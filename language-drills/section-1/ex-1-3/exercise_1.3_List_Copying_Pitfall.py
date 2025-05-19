"""
List Copying Pitfall

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script shows the difference between assigning one list to another
(using `=`) vs. creating a copy using slicing (`[:]`).
"""

# Shared reference: a and b point to the same list
b = [10, 20, 30]
a = b
a.append(40)

print("Shared reference:")
print("a:", a)
print("b:", b)

# Independent copy: a is a shallow copy of b
b = [10, 20, 30]
a = b[:]
a.append(40)

print("\nIndependent copy:")
print("a:", a)
print("b:", b)
