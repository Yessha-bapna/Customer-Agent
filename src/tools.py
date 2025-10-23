from datetime import datetime

# Return policies (days allowed for return)
RETURN_POLICIES = {
    "Acme Noise-Cancelling Headphones": 30,
    "Gamma Stainless Water Bottle": 60,
    "Luna Wireless Mouse": 14,
    "Aurora Yoga Mat": 90,
    "Nimbus Smartwatch": 30
}

def product_return_policy(product_name):
    """Return the allowed number of days for product return."""
    return RETURN_POLICIES.get(product_name, 30)  # default 30 days

def lookup_order(order_id, purchases):
    """Find an order by its ID."""
    for order in purchases:
        if order["order_id"].lower() == order_id.lower():
            return order
    return None

def lookup_order_by_name(product_name, purchases):
    """Find an order by product name."""
    for order in purchases:
        if product_name.lower() in order["product_name"].lower():
            return order
    return None

def is_eligible_for_return(purchase_date, allowed_days):
    """Check if a product is still eligible for return."""
    purchase_date = datetime.fromisoformat(purchase_date).date()
    today = datetime.today().date()
    days_passed = (today - purchase_date).days
    remaining_days = allowed_days - days_passed
    eligible = remaining_days >= 0
    return eligible, remaining_days
