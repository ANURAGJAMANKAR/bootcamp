"""
Sorted with Key

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Sort a list of tuples based on the second element using a key function.
"""

pairs = [(1, 3), (2, 2), (3, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # [(3, 1), (2, 2), (1, 3)]
