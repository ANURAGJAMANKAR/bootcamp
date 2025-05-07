"""
Avoid Nesting

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

def send_invoice(customer):
    """Send invoice if eligible."""
    if not is_active(customer):
        return
    if not has_valid_email(customer):
        return
    email_invoice(customer)

def is_active(customer):
    return customer.get("active", False)

def has_valid_email(customer):
    return "@" in customer.get("email", "")

def email_invoice(customer):
    print(f"Invoicing {customer['email']}")
