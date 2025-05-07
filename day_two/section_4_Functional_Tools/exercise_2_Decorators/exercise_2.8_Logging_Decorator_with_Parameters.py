"""
Logging Decorator with Parameters

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def custom_logger(message):
    """A decorator that logs a custom message before and after the function."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Before {message}")
            result = func(*args, **kwargs)
            print(f"After {message}")
            return result
        return wrapper
    return decorator

# Test custom_logger
@custom_logger("Execution of greet")
def greet(name):
    """Prints a greeting."""
    print(f"Hello, {name}!")

greet("Eve")
