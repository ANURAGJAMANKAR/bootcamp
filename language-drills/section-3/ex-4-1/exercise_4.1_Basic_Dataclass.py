"""
Basic Dataclass

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Define a simple User class using the @dataclass decorator.
"""

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

# Creating an instance of User
user1 = User("Alice", 30)
print(user1.name)  # Output: Alice
print(user1.age)   # Output: 30
