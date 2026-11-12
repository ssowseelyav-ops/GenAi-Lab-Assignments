# Week 1 — First LLM API Call

This is the VS Code/Python version using the Gemini API. It loads `GEMINI_API_KEY` from this folder's `.env`, initializes the Gemini client, sends a prompt, and prints the model response.

## Setup
1. Copy `.env.example` to `.env`.
2. Put your Gemini API key after `GEMINI_API_KEY=`.
3. Install dependencies from the workspace root:
   `python -m pip install -r LAB/Week1/requirements.txt`
4. Run:
   `python LAB/Week1/main.py`
