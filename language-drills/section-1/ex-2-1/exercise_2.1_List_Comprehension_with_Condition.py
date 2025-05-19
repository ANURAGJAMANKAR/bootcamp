"""
List Comprehension with Condition

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script demonstrates a list comprehension with a condition.
It filters out even numbers from a list and squares them.
"""

nums = [1, 2, 3, 4]

# Get squares of even numbers only
result = [x**2 for x in nums if x % 2 == 0]

print("Squared evens:", result)  # Output: [4, 16]
