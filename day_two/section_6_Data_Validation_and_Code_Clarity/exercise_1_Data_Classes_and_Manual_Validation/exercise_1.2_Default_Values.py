"""
Default Values

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from dataclasses import dataclass

@dataclass
class User:
    """User dataclass with a default country."""
    name: str
    age: int
    country: str = "India"

# Example usage
user = User(name="Bob", age=30)
print(user)
