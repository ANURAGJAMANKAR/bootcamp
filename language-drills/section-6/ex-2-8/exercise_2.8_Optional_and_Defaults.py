"""
Optional and Defaults

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    """User model with an optional nickname field."""
    name: str
    age: int
    nickname: Optional[str] = None

# Example usage
user = User(name="Grace", age=33)
print(user)
