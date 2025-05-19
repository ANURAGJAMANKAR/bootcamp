"""
Nested List Comprehension

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script flattens a 2D list using nested list comprehension.
"""

nested = [[1, 2], [3, 4]]

# Flatten the list
flattened = [item for sublist in nested for item in sublist]

print("Flattened list:", flattened)  # Output: [1, 2, 3, 4]
