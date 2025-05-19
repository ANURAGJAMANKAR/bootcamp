"""
Basic Dataclass

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from dataclasses import dataclass

@dataclass
class User:
    """A basic User dataclass with name and age attributes."""
    name: str
    age: int

# Example usage
user = User(name="Alice", age=25)
print(user)
