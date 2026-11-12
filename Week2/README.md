# Week 2 — Provider-agnostic LLM client

This lab uses one common `LLMClient` interface with two providers:
- `gemini` — hosted Gemini API
- `ollama` — local Ollama model (`llama3.2`)

## Setup
1. Copy `.env.example` to `.env` and add your Gemini key if you plan to use Gemini.
2. Install dependencies from the workspace root:
   `python -m pip install -r LAB/Week2/requirements.txt`
3. For the local provider, install Ollama and run `ollama pull llama3.2`.
4. Run from the workspace root:
   `python LAB/Week2/main.py`
5. Choose `gemini` or `ollama` when prompted.

Run tests:
`python -m unittest discover -s LAB/Week2 -p "test_*.py"`
