"""
Compare List vs Generator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import timeit

# Time list comprehension
list_time = timeit.timeit("[x*x for x in range(1000000)]", number=10)
print(f"List comprehension time: {list_time:.6f} seconds")

# Time generator expression
gen_time = timeit.timeit("(x*x for x in range(1000000))", number=10)
print(f"Generator expression time: {gen_time:.6f} seconds")
