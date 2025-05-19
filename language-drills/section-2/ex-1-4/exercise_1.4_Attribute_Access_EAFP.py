"""
Attribute Access EAFP

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Safely access an attribute using getattr() with a fallback default.
"""

class Person:
    def __init__(self, name):
        self.name = name

p = Person("Anurag")
print(getattr(p, "age", "Attribute 'age' not found"))
