"""
Constants

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

MAX_RETRIES = 3  # Maximum allowed retry attempts

def connect_to_server():
    """Attempt to connect, with retry limit."""
    for attempt in range(MAX_RETRIES):
        print(f"Attempt {attempt + 1} to connect...")
