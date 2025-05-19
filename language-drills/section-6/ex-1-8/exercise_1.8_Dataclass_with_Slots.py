"""
Dataclass with Slots

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from dataclasses import dataclass

@dataclass(slots=True)
class User:
    """Space-efficient User dataclass using slots."""
    name: str
    age: int
    country: str = "India"

# Example usage
user = User(name="Henry", age=22)
print(user)
