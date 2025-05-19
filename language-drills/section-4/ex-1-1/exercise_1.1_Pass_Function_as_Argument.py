"""
Pass Function as Argument

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def apply(func, value):
    return func(value)

# Testing apply with different functions
print(apply(abs, -42))  # Output: 42
print(apply(str, 42))   # Output: '42'
print(apply(hex, 42))   # Output: '0x2a'
