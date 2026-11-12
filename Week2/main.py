import os
from pathlib import Path

from dotenv import load_dotenv

from llm_client import GeminiProvider, OllamaProvider, LLMClient

# Load the .env file located beside this script.
load_dotenv(Path(__file__).with_name(".env"))

provider_name = input("Choose provider (gemini/ollama): ").strip().lower()

if provider_name == "gemini":
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "Gemini API key not found. Create LAB/Week2/.env from .env.example "
            "and set GEMINI_API_KEY."
        )
    provider = GeminiProvider(api_key)

elif provider_name == "ollama":
    provider = OllamaProvider("llama3.2")

else:
    raise ValueError("Invalid provider selected. Enter 'gemini' or 'ollama'.")

client = LLMClient(provider)
prompt = input("Enter your question: ")
answer = client.generate(prompt)

print("\nLLM Response:")
print(answer)
