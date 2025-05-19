"""
Model Docstrings

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

from pydantic import BaseModel

class User(BaseModel):
    """
    Represents a system user with personal and access-related information.
    
    This model is used for user profile management and authentication.
    """
    username: str
    email: str

# Example usage
user = User(username="anurag", email="me@example.com")
print(user)
