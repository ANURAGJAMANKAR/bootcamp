"""
Basic Function Decorator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def simple_logger(func):
    """A decorator that logs when a function starts and ends."""
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

# Test simple_logger
@simple_logger
def say_hello(name):
    """Prints a greeting."""
    print(f"Hello, {name}!")

say_hello("Alice")
