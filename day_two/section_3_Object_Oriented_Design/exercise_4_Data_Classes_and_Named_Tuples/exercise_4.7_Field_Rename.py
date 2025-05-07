"""
Field Rename

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Show how invalid field names are auto-renamed when using namedtuple.
"""

from collections import namedtuple

# Trying to use invalid field names (starts with a digit)
try:
    Point = namedtuple("Point", ["1x", "y"])  # Invalid field name '1x'
except ValueError as e:
    print(f"Error: {e}")  # Expect a ValueError for invalid field names

# Namedtuples will automatically rename fields if there are invalid characters.
Point = namedtuple("Point", ["x", "y1"])  # y1 is valid but has a number at the end
point2 = Point(5, 10)
print(point2)  # Output: Point(x=5, y1=10)
