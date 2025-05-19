"""
Custom Validator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel, validator

class User(BaseModel):
    """User model with a name capitalization validator."""
    name: str
    age: int

    @validator("name")
    def name_must_be_capitalized(cls, v):
        if not v[0].isupper():
            raise ValueError("Name must start with a capital letter")
        return v

# Example usage
try:
    user = User(name="edward", age=22)
except Exception as e:
    print("Custom Validation Error:", e)
