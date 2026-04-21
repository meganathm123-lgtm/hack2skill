import os
from google.generativeai import GenerativeModel
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

model = GenerativeModel(api_key=GEMINI_API_KEY)

PROMPT = "Classify this emergency into one of: Fire, Medical, Security. Only return the category."

async def classify_emergency(message: str) -> str:
    prompt = f"{PROMPT}\nMessage: {message}"
    response = model.generate_content(prompt)
    category = response.text.strip()
    if category not in ["Fire", "Medical", "Security"]:
        category = "Security"  # fallback
    return category
