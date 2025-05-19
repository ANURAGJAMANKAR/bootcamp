"""
Custom Object

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Defines a class that returns a default value for missing attributes
using __getattr__.
"""

class SafeObject:
    def __init__(self):
        self.name = "Anurag"

    def __getattr__(self, attr):
        return f"{attr} not found"

obj = SafeObject()
print(obj.name)   # "Anurag"
print(obj.age)    # "age not found"
