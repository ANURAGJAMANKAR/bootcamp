"""
Frozen Dataclass

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Create a frozen dataclass that makes instances immutable.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

# Creating an instance and trying to modify it
user1 = User("Alice", 30)
print(user1.name, user1.age)  # Output: Alice 30

# Attempting to modify an immutable dataclass instance will raise an error
# user1.age = 35  # Uncommenting this will raise a FrozenInstanceError
