"""
Use Chain to Flatten

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import itertools

# Combine [1, 2], [3, 4], [5] into one iterator
flattened = list(itertools.chain([1, 2], [3, 4], [5]))

# Print the flattened list
print(flattened)  # Prints [1, 2, 3, 4, 5]
