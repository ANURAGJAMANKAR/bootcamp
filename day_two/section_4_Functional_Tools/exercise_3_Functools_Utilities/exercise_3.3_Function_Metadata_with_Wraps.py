"""
Function Metadata with Wraps

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from functools import wraps

def my_decorator(func):
    """A simple decorator to demonstrate the use of wraps."""
    @wraps(func)  # Preserves the function metadata
    def wrapper(*args, **kwargs):
        print("Function is about to be called!")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets the person by name."""
    print(f"Hello, {name}!")

# Test the decorator
greet("Charlie")

# Check metadata
print(greet.__name__)  # Should print 'greet'
print(greet.__doc__)   # Should print 'Greets the person by name.'
