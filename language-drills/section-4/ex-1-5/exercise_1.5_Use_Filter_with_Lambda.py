"""
Use Filter with Lambda

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

even_numbers = filter(lambda x: x % 2 == 0, range(10))

# Convert filter object to list for viewing
print(list(even_numbers))  # Output: [0, 2, 4, 6, 8]
