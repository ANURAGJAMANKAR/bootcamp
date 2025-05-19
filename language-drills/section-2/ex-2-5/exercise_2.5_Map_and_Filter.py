"""
Map and Filter

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Use map to double numbers and filter to remove even numbers.
"""

nums = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, nums))
odds = list(filter(lambda x: x % 2 != 0, nums))

print("Doubled:", doubled)
print("Odds:", odds)
