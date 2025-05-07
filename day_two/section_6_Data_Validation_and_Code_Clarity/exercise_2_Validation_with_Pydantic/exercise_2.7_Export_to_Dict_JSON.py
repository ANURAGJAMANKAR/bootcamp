"""
Export to Dict JSON

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel

class User(BaseModel):
    """User model with serialization to dict and JSON."""
    name: str
    age: int

user = User(name="Frank", age=28)
print(user.dict())   # Export as dictionary
print(user.json())   # Export as JSON string
