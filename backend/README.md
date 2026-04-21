# CrisisConnect AI Backend

Production-ready FastAPI backend for CrisisConnect AI — an AI-powered emergency response platform for hospitality environments.

## Features
- User registration & JWT authentication
- Emergency reporting (AI-classified via Google Gemini)
- Firestore database integration
- Rate limiting (slowapi)
- CORS enabled
- Logging
- Modular, clean code

## Project Structure
```
backend/
 ├── main.py
 ├── routes/
 │    ├── emergency.py
 │    ├── auth.py
 ├── services/
 │    ├── gemini_service.py
 │    ├── db_service.py
 ├── models/
 │    ├── schemas.py
 ├── core/
 │    ├── config.py
 │    ├── security.py
 ├── middleware/
 │    ├── rate_limiter.py
 ├── requirements.txt
 ├── .env.example
```

## Setup Instructions

1. **Clone repo & enter backend folder**
2. **Create virtual environment:**
   ```
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Setup environment variables:**
   - Copy `.env.example` to `.env` and fill in your keys.
   - Download Firebase service account JSON and set `FIREBASE_CREDENTIALS_PATH`.
5. **Run server:**
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
6. **API Docs:**
   - Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## Deployment
- Ready for Render, Railway, or Google Cloud Run.
- Use `uvicorn main:app --host 0.0.0.0 --port 8000` as the start command.

## Notes
- For hackathon, CORS allows all origins.
- Rate limit: 10 requests/minute per IP.
- Logging to `logs/backend.log` (auto-created).
- All code is production-quality, modular, and documented.

---

**Happy hacking!**
