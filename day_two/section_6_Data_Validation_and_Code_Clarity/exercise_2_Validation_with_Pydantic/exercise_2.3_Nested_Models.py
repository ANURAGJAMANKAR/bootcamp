"""
Nested Models

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel

class Profile(BaseModel):
    """Profile model representing user metadata."""
    bio: str
    website: str

class User(BaseModel):
    """User model that includes a nested Profile model."""
    name: str
    age: int
    profile: Profile

# Example usage
data = {
    "name": "Charlie",
    "age": 30,
    "profile": {
        "bio": "Data scientist.",
        "website": "https://example.com"
    }
}
user = User(**data)
print(user)
