"""
Memoization Decorator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def memoize(func):
    """A decorator that caches the function results for repeated calls."""
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Fetching cached result for {args}")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

# Test memoize
@memoize
def expensive_computation(x):
    """Simulates an expensive computation."""
    print(f"Computing for {x}...")
    return x * 2

print(expensive_computation(4))
print(expensive_computation(4))  # Cached result
