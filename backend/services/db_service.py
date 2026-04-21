import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
from datetime import datetime
import uuid

load_dotenv()
FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)
db = firestore.client()

async def store_emergency(message: str, category: str):
    doc_id = str(uuid.uuid4())
    data = {
        "id": doc_id,
        "type": category,
        "message": message,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "Active"
    }
    db.collection("emergencies").document(doc_id).set(data)
    return data

async def get_all_emergencies():
    docs = db.collection("emergencies").stream()
    return [doc.to_dict() for doc in docs]

async def update_emergency_status(id: str, status: str):
    doc_ref = db.collection("emergencies").document(id)
    if not doc_ref.get().exists:
        return False
    doc_ref.update({"status": status})
    return True

async def create_user(username: str, password: str):
    doc_id = str(uuid.uuid4())
    data = {"id": doc_id, "username": username, "password": password}
    db.collection("users").document(username).set(data)
    return {"id": doc_id, "username": username}

async def get_user_by_username(username: str):
    doc = db.collection("users").document(username).get()
    return doc.to_dict() if doc.exists else None
