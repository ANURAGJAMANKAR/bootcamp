"""
Post Init Validation

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from dataclasses import dataclass

@dataclass
class User:
    """User dataclass that validates age after initialization."""
    name: str
    age: int
    country: str = "India"

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative.")

# Example usage
try:
    user = User(name="Charlie", age=-5)
except ValueError as e:
    print("Validation Error:", e)
