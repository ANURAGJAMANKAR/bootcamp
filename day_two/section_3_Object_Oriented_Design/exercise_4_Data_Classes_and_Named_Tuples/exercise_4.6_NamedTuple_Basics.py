"""
NamedTuple Basics

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Define a Point using collections.namedtuple and access its fields.
"""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

# Creating an instance of Point
point1 = Point(10, 20)
print(point1.x)  # Output: 10
print(point1.y)  # Output: 20
