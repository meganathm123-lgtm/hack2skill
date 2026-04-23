import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import uuid

# 🔐 Load Firebase credentials from ENV (GitHub Secret → Cloud Run)
firebase_json = os.getenv("FIREBASE_CREDENTIALS")

if not firebase_json:
    raise Exception("FIREBASE_CREDENTIALS not found in environment variables")

# Initialize Firebase
if not firebase_admin._apps:
    cred_dict = json.loads(firebase_json)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()


# 🚨 STORE EMERGENCY (UPDATED)
async def store_emergency(message: str, category: str, priority: str, user: str):
    doc_id = str(uuid.uuid4())

    data = {
        "id": doc_id,
        "type": category,
        "priority": priority,   # ✅ NEW
        "message": message,
        "user": user,           # ✅ NEW
        "timestamp": datetime.utcnow().isoformat(),
        "status": "Active"
    }

    db.collection("emergencies").document(doc_id).set(data)
    return data


# 📊 GET ALL EMERGENCIES
async def get_all_emergencies():
    docs = db.collection("emergencies").stream()
    return [doc.to_dict() for doc in docs]


# 🔁 UPDATE STATUS
async def update_emergency_status(id: str, status: str):
    doc_ref = db.collection("emergencies").document(id)

    if not doc_ref.get().exists:
        return False

    doc_ref.update({"status": status})
    return True


# 👤 CREATE USER
async def create_user(username: str, password: str):
    doc_id = str(uuid.uuid4())

    data = {
        "id": doc_id,
        "username": username,
        "password": password
    }

    db.collection("users").document(username).set(data)

    return {
        "id": doc_id,
        "username": username
    }


# 🔍 GET USER
async def get_user_by_username(username: str):
    doc = db.collection("users").document(username).get()
    return doc.to_dict() if doc.exists else None