
# Product Return Support Agent 

This project is a **Customer Support AI Agent** built using **Python**, **LangGraph**, and **Gemini API**.  
It helps users check whether a product is still eligible for return based on its order date and store policy.

---

## ✅ Features
✔ Uses **Generative AI (Gemini model)** to understand customer queries  
✔ Follows **React Pattern (Reason → Act → Respond)** using LangGraph  
✔ Includes **Mock Purchase Data** (5 example orders)  
✔ Implements tool-based logic:
- `lookup_order`
- `lookup_order_by_name`
- `product_return_policy`
- `is_eligible_for_return`

✔ Runs as an **interactive console chatbot**

---

## 🧩 Project Structure
```
return_agent/
│
├── Data/
│   └── mock_purchases.json
│
├── src/
│   ├── tools.py
│   ├── graph_agent.py
│   ├── run.py
│   └── __init__.py
│
├── .env
└── README.md
```

---

## 🔑 Environment Setup

### 1️⃣ Create and Activate Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 2️⃣ Install Dependencies
```bash
pip install langgraph google-generativeai python-dotenv or pip install -r requirements.txt
```

### 3️⃣ Create `.env` file
In project root:
```
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

You can generate an API key from:  
➡ https://aistudio.google.com/app/apikey

---

## 🗃 Mock Data File

In `Data/mock_purchases.json`:
```json
[
  {
    "order_id": "ORD-1001",
    "product_name": "Acme Noise-Cancelling Headphones",
    "purchase_date": "2025-09-20",
    "price": 129.99
  },
  {
    "order_id": "ORD-1002",
    "product_name": "Gamma Stainless Water Bottle",
    "purchase_date": "2025-07-10",
    "price": 24.99
  },
  {
    "order_id": "ORD-1003",
    "product_name": "Luna Wireless Mouse",
    "purchase_date": "2025-10-12",
    "price": 39.50
  },
  {
    "order_id": "ORD-1004",
    "product_name": "Aurora Yoga Mat",
    "purchase_date": "2025-04-03",
    "price": 49.00
  },
  {
    "order_id": "ORD-1005",
    "product_name": "Nimbus Smartwatch",
    "purchase_date": "2025-09-01",
    "price": 199.00
  }
]
```

---

## ▶️ How to Run the Agent

In terminal:
```bash
python src/run.py
```

Example Usage:
```
product Return Support Agent
Type 'exit' to quit

You: Can I return my Nimbus Smartwatch?
Agent: ✅ Yes! Your product is still eligible for return with X days left.
```

Stop anytime using:
```
exit
```

---

## 💡 Example Queries to Test
| User Query | What Happens |
|-----------|--------------|
| "Is order ORD-1003 still eligible?" | Looks up order and returns eligibility |
| "Can I return my yoga mat?" | Matches product name and calculates |
| "How many days left to return my smartwatch?" | Uses date rules |
| "I bought the headphones in September. Can I return them?" | Gemini extracts product intent |
| "I want refund info for ORD‑1002" | Expandable future improvement |

---

## 🧠 Tech Used
| Component | Purpose |
|----------|---------|
| **Gemini API** | Reasoning + Response |
| **LangGraph** | Workflow control |
| **Python Functions** | Tool logic for returns |
| **JSON Data** | Mock purchases database |

---

## 🚀 Future Enhancements (Optional)
- Refund calculator tool
- Multi-turn memory
- Web UI version
- Logging & analytics
- Unit test automation

---


