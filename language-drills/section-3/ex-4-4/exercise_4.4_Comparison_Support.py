"""
Comparison Support

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Dataclasses automatically support comparison methods like __eq__ for object comparison.
"""

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

# Creating instances and comparing them
user1 = User("Alice", 30)
user2 = User("Alice", 30)
user3 = User("Bob", 25)

print(user1 == user2)  # Output: True (Same name and age)
print(user1 == user3)  # Output: False (Different name and age)
