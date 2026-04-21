🚀 **HACKATHON PLAN (READ THIS FIRST — NO CONFUSION)**

## 🧭 Overall Flow

User → Frontend → Backend → Gemini AI → Database → Dashboard

---

## 🏗️ Architecture

[ User (Guest/Staff) ]
↓
[ Frontend (React / HTML) ]
↓
[ Backend API (FastAPI) ]
↓
[ Gemini API (AI Classification) ]
↓
[ Firebase Firestore (DB) ]
↓
[ Admin Dashboard ]

---

## ⚙️ Tech Stack (FIXED — don’t change)

Frontend:

* React OR HTML/CSS/JS
* Axios

Backend:

* FastAPI (Python)
* Gemini API
* Firebase Firestore
* Uvicorn

PPT:

* Canva / PowerPoint
* Diagrams + Demo Script

---

## 👥 Roles

### 👨‍💻 Backend

* Create APIs:

  * `/report-emergency`
  * `/get-alerts`
* Integrate Gemini (classify: Fire / Medical / Security)
* Store in Firebase
* Enable CORS

Example:
{
"type": "Fire",
"message": "Smoke in kitchen",
"time": "...",
"status": "Active"
}

---

### 🎨 Frontend

Page 1:

* Emergency input (text or buttons)
* Send to backend

Page 2:

* Dashboard:

  * Type
  * Message
  * Status

API:
POST /report-emergency
{ message: "Fire in kitchen" }

---

### 📊 PPT

Slides:

1. Problem
2. Solution
3. Features
4. Architecture
5. Tech Stack
6. Demo Flow
7. Future Scope

---

## 🔗 Flow

1. User sends input
2. Frontend → Backend
3. Backend → Gemini
4. Gemini → category
5. Store in Firebase
6. Show in dashboard

---

## 🧪 MVP (ONLY THIS)

* 1 working API
* 1 AI classification
* 1 dashboard
* 1 deployed link

---

## ⚡ PLAN

### Today:

Backend → Setup FastAPI + Gemini
Frontend → Build UI
PPT → Start slides

### Tomorrow:

Backend → APIs
Frontend → Connect APIs
PPT → Architecture diagram

---

## ⚠️ RULES

* No extra features
* No changing idea
* No overdesign

👉 Focus = Working demo
