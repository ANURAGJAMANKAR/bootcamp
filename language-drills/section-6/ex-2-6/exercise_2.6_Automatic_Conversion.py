"""
Automatic Conversion

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel

class User(BaseModel):
    """User model that demonstrates automatic type coercion."""
    age: int

# Pydantic converts the string "42" to an int
user = User(age="42")
print(user)  # age=42
