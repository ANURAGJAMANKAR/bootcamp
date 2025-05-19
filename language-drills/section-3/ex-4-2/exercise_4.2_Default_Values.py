"""
Default Values

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Add a default value for the age attribute and test object creation with and without it.
"""

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0  # Default age is 0

# Creating instances with and without the default age value
user1 = User("Alice")
user2 = User("Bob", 25)

print(user1.name, user1.age)  # Output: Alice 0
print(user2.name, user2.age)  # Output: Bob 25
