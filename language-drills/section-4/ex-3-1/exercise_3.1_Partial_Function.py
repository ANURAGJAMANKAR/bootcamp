"""
Partial Function

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import functools

# Create a partial function that converts strings to integers with base 2
binary_to_int = functools.partial(int, base=2)

# Test the partial function
print(binary_to_int('1010'))  # Should print 10
print(binary_to_int('1101'))  # Should print 13
