import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# Load the .env file located beside this script.
load_dotenv(Path(__file__).with_name(".env"))

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "Gemini API key not found. Create LAB/Week1/.env from .env.example "
        "and set GEMINI_API_KEY."
    )

client = genai.Client(api_key=api_key)

# Change this prompt to try the experiments in the Week 1 lab guide.
prompt = "What is Artificial Intelligence? Explain in simple words."

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
)

print("\nLLM Response:")
print(response.text)
