"""
Use Islice

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import itertools

# Skip the first 3 elements and take the next 4 elements from a range
sliced = list(itertools.islice(range(10), 3, 7))

# Print the sliced list
print(sliced)  # Prints [3, 4, 5, 6]
