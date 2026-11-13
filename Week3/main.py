"""Week 3: interactive Gemini/Ollama client with MongoDB monitoring."""
import os
from pathlib import Path

from dotenv import load_dotenv

from llm_client import GeminiProvider, OllamaProvider, LLMClient
from usage_logger import UsageLogger

load_dotenv(Path(__file__).with_name(".env"), override=True)


def main():
    usage_logger = UsageLogger()
    try:
        provider_name = input("Choose provider (gemini/ollama): ").strip().lower()

        if provider_name == "gemini":
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("Gemini API key not found in Week3/.env")
            provider = GeminiProvider(api_key)

        elif provider_name == "ollama":
            provider = OllamaProvider("llama3.2")

        else:
            raise ValueError("Invalid provider selected. Enter 'gemini' or 'ollama'.")

        client = LLMClient(provider, usage_logger)
        prompt = input("Enter your question: ").strip()
        if not prompt:
            raise ValueError("Please enter a question.")

        answer = client.generate(prompt)
        print("\nLLM Response:")
        print(answer)

    finally:
        usage_logger.close()


if __name__ == "__main__":
    main()
