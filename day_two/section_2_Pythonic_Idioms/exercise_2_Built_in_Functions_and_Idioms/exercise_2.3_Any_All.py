"""
Any All

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Use any() to check if *any* number is negative,
and all() to check if *all* numbers are positive.
"""

numbers = [1, 2, -3, 4]

print(any(n < 0 for n in numbers))  # True
print(all(n > 0 for n in numbers))  # False
