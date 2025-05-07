"""
Log Decorator with Wraps

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from functools import wraps

def log_decorator(func):
    """A decorator that logs before and after executing a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished with result {result}")
        return result
    return wrapper

# Test log_decorator
@log_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

add(5, 3)
