"""
Field Descriptions

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel, Field

class User(BaseModel):
    """User model with a field description for email."""
    email: str = Field(..., description="User's email address")

# Example usage
user = User(email="alice@example.com")
print(user)
