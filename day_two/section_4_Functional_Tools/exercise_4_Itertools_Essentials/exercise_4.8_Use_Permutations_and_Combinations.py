"""
Use Permutations and Combinations

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import itertools

# Generate all pairs (2-length permutations) from [1, 2, 3]
pairs = list(itertools.permutations([1, 2, 3], 2))
print(pairs)  # Prints [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Generate all triples (3-length combinations) from [1, 2, 3]
triples = list(itertools.combinations([1, 2, 3], 3))
print(triples)  # Prints [(1, 2, 3)]
