"""
Timing Decorator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import time

def timer(func):
    """A decorator that prints the time taken by the function to execute."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Test timer
@timer
def slow_function():
    """Simulates a slow function."""
    time.sleep(2)

slow_function()
