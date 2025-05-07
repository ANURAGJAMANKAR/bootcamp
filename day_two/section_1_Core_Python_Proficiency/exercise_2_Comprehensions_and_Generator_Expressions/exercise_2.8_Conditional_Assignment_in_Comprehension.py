"""
Conditional Assignment in Comprehension

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script replaces all negative numbers in a list with 0
using conditional logic inside a list comprehension.
"""

numbers = [-3, 5, -1, 7]

# Replace negatives with 0
non_negative = [x if x >= 0 else 0 for x in numbers]

print("Replaced negatives:", non_negative)  # Output: [0, 5, 0, 7]
