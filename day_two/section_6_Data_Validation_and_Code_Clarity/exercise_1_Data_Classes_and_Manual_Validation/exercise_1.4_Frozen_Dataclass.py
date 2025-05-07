"""
Frozen Dataclass

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    """Immutable User dataclass."""
    name: str
    age: int
    country: str = "India"

# Example usage
user = User(name="Diana", age=28)
print(user)

# Attempting to modify should raise a FrozenInstanceError
try:
    user.age = 29
except Exception as e:
    print("Mutation Error:", e)
