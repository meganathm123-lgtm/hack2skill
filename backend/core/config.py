import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    FIREBASE_CREDENTIALS: str = os.getenv("FIREBASE_CREDENTIALS")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

settings = Settings()
