"""
Uncached Recursive Function

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import time

# Regular recursive Fibonacci without caching
def uncached_fib(n):
    if n <= 1:
        return n
    return uncached_fib(n-1) + uncached_fib(n-2)

# Test uncached Fibonacci performance
start_time = time.time()
print(uncached_fib(30))
print(f"Uncached Fibonacci time: {time.time() - start_time:.4f} seconds")

# Fibonacci with lru_cache (memoized)
start_time = time.time()
print(fib(30))
print(f"LRU Cached Fibonacci time: {time.time() - start_time:.4f} seconds")
