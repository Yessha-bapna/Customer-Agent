import os, json
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
import google.generativeai as genai
from src.tools import (
    lookup_order, lookup_order_by_name,
    product_return_policy, is_eligible_for_return
)

# Load env + setup Gemini if available
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load mock data from project Data folder (robust path)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
mock_path = os.path.join(BASE_DIR, "Data", "mock_purchases.json")
if not os.path.exists(mock_path):
    mock_path = os.path.join(BASE_DIR, "data", "mock_purchases.json")

with open(mock_path, "r", encoding="utf-8") as f:
    purchases = json.load(f)


from typing import TypedDict, Any

class AgentState(TypedDict):
    user_input: str
    reasoning: str
    action_result: Any
    final_response: str


# ---- Nodes ----
def reason_node(state: AgentState):
    """LLM interprets the user's query."""
    user_input = state["user_input"]
    prompt = f"""
    You are a customer support reasoning agent.
    Analyze this query: "{user_input}"
    Identify:
    1. What is the user asking (intent)?
    2. Which product or order might be mentioned?
    Return a short reasoning summary.
    """
    model = genai.GenerativeModel("gemini-2.5-flash")
    reasoning = model.generate_content(prompt).text
    state["reasoning"] = reasoning
    return state


def act_node(state: AgentState):
    """Decide what tool to use and perform the action."""
    reasoning = state["reasoning"]
    user_input = state["user_input"]

    # Try to find product or order
    found = None
    for order in purchases:
        if order["order_id"].lower() in user_input.lower():
            found = order
            break
        if order["product_name"].lower() in user_input.lower():
            found = order
            break

    if not found:
        state["action_result"] = "No matching order found. Ask for order ID or product name."
        return state

    allowed_days = product_return_policy(found["product_name"])
    eligible, remaining = is_eligible_for_return(found["purchase_date"], allowed_days)

    result = {
        "product": found["product_name"],
        "order_id": found["order_id"],
        "allowed_days": allowed_days,
        "eligible": eligible,
        "remaining": remaining
    }
    state["action_result"] = result
    return state


def respond_node(state: AgentState):
    """LLM creates the final user-facing response."""
    action = state["action_result"]

    model = genai.GenerativeModel("gemini-2.5-flash")
    if isinstance(action, str):  
        state["final_response"] = action
        print("\nAgent:", action)
        return state

    eligible = "eligible" if action["eligible"] else "not eligible"
    prompt = f"""
    Write a friendly customer support reply based on this:
    Product: {action['product']}
    Order ID: {action['order_id']}
    Return window: {action['allowed_days']} days
    Eligibility: {eligible}
    Days remaining: {action['remaining']}
    """

    response = model.generate_content(prompt).text
    state["final_response"] = response
    print("\nAgent:", response)
    return state

# ---- Build the graph ----
graph = StateGraph(AgentState)
graph.add_node("reason", reason_node)
graph.add_node("act", act_node)
graph.add_node("respond", respond_node)

graph.set_entry_point("reason")
graph.add_edge("reason", "act")
graph.add_edge("act", "respond")
graph.add_edge("respond", END)

app = graph.compile()
