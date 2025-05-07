"""
Custom Method

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from dataclasses import dataclass

@dataclass
class User:
    """User dataclass with an is_adult() method."""
    name: str
    age: int
    country: str = "India"

    def is_adult(self) -> bool:
        """Returns True if the user is 18 or older."""
        return self.age >= 18

# Example usage
user = User(name="Eva", age=17)
print(user.is_adult())  # Output: False
