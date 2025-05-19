"""
Retry Mechanism Decorator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

import random

def retry(max_retries=3):
    """A decorator that retries a function if it raises an exception."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    print(f"Attempt {retries} failed: {e}")
            print("Max retries reached.")
        return wrapper
    return decorator

# Test retry
@retry(max_retries=3)
def unstable_function():
    """Simulates a function that may fail randomly."""
    if random.choice([True, False]):
        raise ValueError("Random failure!")
    return "Success!"

print(unstable_function())
