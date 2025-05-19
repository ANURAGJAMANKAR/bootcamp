"""
Closure with Lambda

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def make_multiplier(factor):
    return lambda x: x * factor

# Create a multiplier function that multiplies by 3
multiplier_by_3 = make_multiplier(3)
print(multiplier_by_3(5))  # Output: 15
