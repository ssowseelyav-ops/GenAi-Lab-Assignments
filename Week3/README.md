# Week 3 — LLM Monitoring with MongoDB

This VS Code version follows the supplied Week-3 handout and extends the provider-agnostic client from Week 2.

## Files
- `main.py` — choose Gemini or Ollama and submit a prompt.
- `llm_client.py` — common provider interface, token counts, latency, cost estimate and retries.
- `usage_logger.py` — MongoDB connection and usage logging.
- `test_client.py` — offline unit test with a fake provider/logger.
- `requirements.txt` — dependencies.
- `.env.example` — credential and pricing placeholders.

## 1. Set up MongoDB Atlas
Follow the handout: create a free cluster, create a database user, add your current IP under Network Access, then copy the Python driver connection string. Avoid `0.0.0.0/0`.

## 2. Configure `.env`
Copy `.env.example` to `.env` in this folder. Fill in:
- `GEMINI_API_KEY`
- `MONGODB_URI`
- `GEMINI_INPUT_PRICE_PER_MILLION`
- `GEMINI_OUTPUT_PRICE_PER_MILLION`

The two pricing values are USD per one million tokens. They default to `0`, so set them to the current rates for your Gemini model if you want a cost estimate. Verify current Google pricing; rates can change.

Never share `.env` or commit it to Git. No real API keys or database credentials are included.

## 3. Install from the workspace root
Activate the existing root virtual environment, then run:

```powershell
python -m pip install -r LAB/Week3/requirements.txt
```

## 4. Run the unit test
From the workspace root:

```powershell
python -m unittest discover -s LAB/Week3 -p "test_*.py"
```

The test uses a fake provider and fake logger, so it does not need a real API key or MongoDB connection.

## 5. Run the application
From the workspace root:

```powershell
python LAB/Week3/main.py
```

Choose `gemini` or `ollama`, then enter a prompt.

For Ollama, install/start Ollama and download the model once:

```powershell
ollama pull llama3.2
```

## MongoDB output
The program creates database `llm_monitoring` and collection `api_usage`. Each successful request or final failed request is logged with provider, model, token counts (when available), elapsed milliseconds, estimated cost and retry count.

The latency value includes time spent waiting through retries, as described in the handout. Failed calls have unknown token usage and cost. Ollama token counts come from its local generate endpoint; its hosted API cost is recorded as zero, not including electricity or hardware.

## Important
The Gemini and Ollama calls have request timeouts. The common client makes up to three attempts for selected temporary errors, with 1-second and 2-second waits. The Gemini SDK may have internal retries too; avoid stacking retry policies unintentionally in production.
