"""
Field Aliases

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel, Field

class User(BaseModel):
    """User model with an alias for the 'id' field."""
    id: int = Field(..., alias="user_id")

# Example input with alias key
data = {"user_id": 123}
user = User(**data)
print(user)
