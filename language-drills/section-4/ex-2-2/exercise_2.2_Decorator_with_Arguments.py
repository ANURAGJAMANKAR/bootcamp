"""
Decorator with Arguments

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def prefix_printer(prefix):
    """A decorator that prints a given prefix before the function's name."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} {func.__name__} started")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Test prefix_printer
@prefix_printer("Calling")
def greet(name):
    """Greets the person."""
    print(f"Hello, {name}!")

greet("Bob")
