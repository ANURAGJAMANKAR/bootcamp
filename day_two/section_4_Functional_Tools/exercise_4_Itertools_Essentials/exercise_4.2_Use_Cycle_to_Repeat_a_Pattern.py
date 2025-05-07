"""
Use Cycle to Repeat a Pattern

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import itertools

# Cycle through ["red", "green", "blue"]
colors = itertools.cycle(["red", "green", "blue"])

# Print the first 6 items from the cycle
for _ in range(6):
    print(next(colors))  # Prints "red", "green", "blue", "red", "green", "blue"
