"""
Lru Cache Memoization

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from functools import lru_cache

@lru_cache(maxsize=None)  # Cache all results for the Fibonacci sequence
def fib(n):
    """Recursive Fibonacci function with memoization."""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Test the Fibonacci function with memoization
print(fib(30))  # Should be much faster with the cache
