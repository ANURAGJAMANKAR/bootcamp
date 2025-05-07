"""
Debug Information Decorator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def debug_info(func):
    """A decorator that prints the function name, arguments, and return value."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Test debug_info
@debug_info
def add(a, b):
    """Adds two numbers."""
    return a + b

add(5, 7)
