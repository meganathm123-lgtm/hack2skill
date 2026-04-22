import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize client (new SDK)
client = genai.Client(api_key=GEMINI_API_KEY)

# Models (primary + fallback)
PRIMARY_MODEL = "gemini-2.5-flash"
FALLBACK_MODEL = "gemini-1.5-flash"


PROMPT = """
You are an emergency classification system.

Classify the message into ONLY one category:
Fire, Medical, Security.

Return ONLY one word: Fire or Medical or Security.
"""


async def classify_emergency(message: str) -> str:
    full_prompt = f"{PROMPT}\nMessage: {message}"

    category = "Security"  # default safe fallback

    try:
        # 🔹 Primary model
        response = client.models.generate_content(
            model=PRIMARY_MODEL,
            contents=full_prompt
        )

        if hasattr(response, "text") and response.text:
            category = response.text.strip().capitalize()

    except Exception as e:
        print("Primary model failed:", e)

        try:
            # 🔹 Fallback model
            response = client.models.generate_content(
                model=FALLBACK_MODEL,
                contents=full_prompt
            )

            if hasattr(response, "text") and response.text:
                category = response.text.strip().capitalize()

        except Exception as e:
            print("Fallback model failed:", e)

    # 🔹 Final normalization (VERY IMPORTANT)
    if category not in ["Fire", "Medical", "Security"]:
        category = "Security"

    return category


# 🔥 NEW: Priority assignment
def assign_priority(category: str) -> str:
    if category == "Fire":
        return "High"
    elif category == "Medical":
        return "Medium"
    else:
        return "Low"