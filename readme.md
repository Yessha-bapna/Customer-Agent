# Customer Agent

This small project is a terminal-based customer support agent that can answer questions about product return eligibility using a mock purchases dataset.

## Quick overview
- Main script: `run_console.py` — starts a terminal REPL to ask questions.
- Agent implementation: `src/graph_agent.py` — orchestrates reasoning, action lookup, and response generation.
- Tools: `src/tools.py` — contains return policies and the `is_eligible_for_return` helper.
- Mock data: `Data/mock_purchases.json` — contains sample orders used for testing.

## Requirements
- Python 3.10 or newer
- The project expects these Python packages (install with pip):
  - python-dotenv
  - google-generativeai
  - langgraph

Install dependencies (recommended in a virtual environment):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # or pip install python-dotenv google-generativeai langgraph
```

If you plan to use Gemini (recommended for best responses) set your Gemini API key in an environment variable named `GEMINI_API_KEY` (or in a `.env` file):

```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
```

## Run the agent

Start the console:

```powershell
python .\run_console.py
```

Type questions and press Enter. Type `exit` or `quit` to stop.

## Where the data comes from
- The mock data used by the agent lives at `Data/mock_purchases.json` and is the source of truth for return-eligibility checks in demo/test runs.

## Example queries to try
Use these example prompts in the console to test behavior. They exercise order lookup, product-name lookup, and return-policy responses.

- Ask by order id:
  - "Can I return order ORD-1005?"
  - "What's the return policy for ORD-1002?"

- Ask by product name:
  - "Can I return my Nimbus Smartwatch?"
  - "I bought the Luna Wireless Mouse — is it eligible for return?"

- Edge-case / follow-ups to test error handling:
  - "Can I return ORD-9999?" (non-existent order)
  - "How many days left to return my Acme Noise-Cancelling Headphones?"

## What the agent checks
- Lookup: searches `Data/mock_purchases.json` by `order_id` or `product_name`.
- Policy: `src/tools.py` maps product names to allowed return days.
- Eligibility: `is_eligible_for_return(purchase_date, allowed_days)` computes days remaining and eligibility.

## If something doesn't work
- Ensure `Data/mock_purchases.json` exists and is readable.
- Make sure required packages are installed and `GEMINI_API_KEY` is set if you want to use the Gemini model.
- If you prefer not to use Gemini, you can run the repo with local fallbacks (I previously added such fallbacks). If you removed them, re-install the packages.

## Development notes
- `src/graph_agent.py` is the primary integration point. If you want to test `is_eligible_for_return` separately, open a Python shell and run:

```python
from src.tools import is_eligible_for_return, product_return_policy
order = next(o for o in __import__('json').load(open('Data/mock_purchases.json')) if o['order_id'] == 'ORD-1005')
print(is_eligible_for_return(order['purchase_date'], product_return_policy(order['product_name'])))
```

## Suggested example questions to include in UI or tests
- "Can I return my Nimbus Smartwatch? Order ORD-1005"
- "Is ORD-1002 eligible for return?"
- "What's the return window for Luna Wireless Mouse?"
- "How many days do I have left to return ORD-1004?"

---
If you'd like, I can also add a `requirements.txt`, example unit tests for `is_eligible_for_return`, or commit these changes to git. Which would you like next?
