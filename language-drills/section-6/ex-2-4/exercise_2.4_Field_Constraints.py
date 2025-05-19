"""
Field Constraints

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel, conint, constr

class User(BaseModel):
    """User model with constraints on age and username."""
    username: constr(min_length=3)
    age: conint(gt=0)

# Example usage
user = User(username="dave", age=25)
print(user)
