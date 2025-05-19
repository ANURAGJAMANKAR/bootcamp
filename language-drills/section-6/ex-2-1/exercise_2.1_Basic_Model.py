"""
Basic Model

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel

class User(BaseModel):
    """Basic User model with name and age fields."""
    name: str
    age: int

# Example usage
data = {"name": "Alice", "age": 25}
user = User(**data)
print(user)
