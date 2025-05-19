"""
Generator Expression

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script creates a generator expression that yields squares of numbers
from 0 to 4, then prints each value.
"""

# Generator that yields n squared
gen = (n*n for n in range(5))

# Print items one by one
for value in gen:
    print("Generated:", value)
