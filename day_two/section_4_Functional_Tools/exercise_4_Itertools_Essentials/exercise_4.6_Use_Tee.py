"""
Use Tee

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import itertools

# Duplicate the iterator
original_iter = iter([1, 2, 3, 4, 5])
iter1, iter2 = itertools.tee(original_iter, 2)

# Iterate independently on both iterators
print(list(iter1))  # Prints [1, 2, 3, 4, 5]
print(list(iter2))  # Prints [1, 2, 3, 4, 5]
