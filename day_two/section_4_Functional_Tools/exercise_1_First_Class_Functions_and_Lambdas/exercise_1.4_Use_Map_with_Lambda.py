"""
Use Map with Lambda

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

numbers = [1, 2, 3]
squared = map(lambda x: x ** 2, numbers)

# Convert map object to list for viewing
print(list(squared))  # Output: [1, 4, 9]
