"""
Custom Method in Dataclass

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Add a method `is_adult()` to the dataclass to check if the user is an adult (age >= 18).
"""

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def is_adult(self):
        return self.age >= 18

# Creating an instance and checking if the user is an adult
user1 = User("Alice", 30)
user2 = User("Bob", 17)

print(user1.is_adult())  # Output: True
print(user2.is_adult())  # Output: False
