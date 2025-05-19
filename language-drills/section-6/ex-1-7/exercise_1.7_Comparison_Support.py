"""
Comparison Support

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from dataclasses import dataclass

@dataclass
class User:
    """User dataclass with comparison support."""
    name: str
    age: int
    country: str = "India"

# Example usage
user1 = User(name="Grace", age=40)
user2 = User(name="Grace", age=40)

print(user1 == user2)  # Output: True
