"""
Zip

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Combine elements of two lists into tuples using zip().
"""

nums = [1, 2, 3]
letters = ['a', 'b', 'c']

combined = list(zip(nums, letters))
print(combined)  # [(1, 'a'), (2, 'b'), (3, 'c')]
