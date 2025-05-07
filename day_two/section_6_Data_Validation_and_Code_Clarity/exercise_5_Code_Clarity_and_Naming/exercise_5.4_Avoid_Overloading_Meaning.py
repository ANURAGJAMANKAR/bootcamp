"""
Avoid Overloading Meaning

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

def process_customer_orders(order_list: list[dict]):
    """Processes a list of customer orders."""
    for order in order_list:
        print(f"Processing order ID: {order['id']}")
