"""
Use Count to Generate IDs

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import itertools

# Create an infinite ID generator
id_generator = itertools.count(start=1)

# Generate and print the first 5 IDs
for _ in range(5):
    print(next(id_generator))  # Prints 1, 2, 3, 4, 5
