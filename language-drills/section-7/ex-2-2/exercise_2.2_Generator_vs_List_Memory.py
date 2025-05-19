"""
Generator vs List Memory

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import sys

# Create a list and generator for the range of numbers
num_list = [x for x in range(1000000)]
num_gen = (x for x in range(1000000))

# Compare memory size using sys.getsizeof()
print(f"List memory size: {sys.getsizeof(num_list)} bytes")
print(f"Generator memory size: {sys.getsizeof(num_gen)} bytes")
