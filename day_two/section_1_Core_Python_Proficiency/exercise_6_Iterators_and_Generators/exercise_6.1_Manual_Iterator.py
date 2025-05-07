"""
Manual Iterator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Creates an iterator manually from a list
and walks through it using next().
"""

numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
