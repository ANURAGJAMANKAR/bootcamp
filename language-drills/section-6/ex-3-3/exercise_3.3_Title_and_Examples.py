"""
Title and Examples

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel, Field

class User(BaseModel):
    """User model with titles and examples for better documentation."""
    name: str = Field(..., title="Full Name", example="Alice")
    age: int = Field(..., title="Age of the user", example=30)

# Example usage
user = User(name="Bob", age=32)
print(user)
