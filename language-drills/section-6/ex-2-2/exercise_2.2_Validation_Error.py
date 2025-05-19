"""
Validation Error

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    """User model that validates age as an integer."""
    name: str
    age: int

# Invalid input with age as a string
try:
    user = User(name="Bob", age="not a number")
except ValidationError as e:
    print("Validation Error:\n", e)
