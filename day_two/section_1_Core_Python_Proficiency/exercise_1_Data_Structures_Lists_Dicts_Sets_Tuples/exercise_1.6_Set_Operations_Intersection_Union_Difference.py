"""
Set Operations Intersection Union Difference

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script demonstrates basic set operations:
- Intersection
- Union
- Difference
"""

a = {1, 2, 3}
b = {3, 4}

# Find common elements
print("Intersection:", a & b)

# Combine both sets
print("Union:", a | b)

# Elements in a not in b
print("Difference (a - b):", a - b)
