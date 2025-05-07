"""
Factory Default for Lists

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    """User dataclass with tags as a list of strings."""
    name: str
    age: int
    country: str = "India"
    tags: List[str] = field(default_factory=list)

# Example usage
user = User(name="Frank", age=35)
print(user.tags)  # Output: []
