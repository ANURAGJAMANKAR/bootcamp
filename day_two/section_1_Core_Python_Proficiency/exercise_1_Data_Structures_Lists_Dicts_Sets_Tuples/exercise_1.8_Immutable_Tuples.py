"""
Immutable Tuples

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script attempts to modify a tuple and demonstrates
that tuples are immutable by catching the resulting error.
"""

immutable_tuple = (1, 2, 3)

try:
    # This will raise a TypeError because tuples can't be changed
    immutable_tuple[0] = 99
except TypeError as e:
    print("Error:", e)
