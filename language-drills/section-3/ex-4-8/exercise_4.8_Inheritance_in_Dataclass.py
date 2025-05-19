"""
Inheritance in Dataclass

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Create an AdminUser class that inherits from User and adds an access_level attribute.
"""

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

@dataclass
class AdminUser(User):
    access_level: int

# Creating instances and testing
admin1 = AdminUser("Alice", 30, 5)
print(admin1.name, admin1.age, admin1.access_level)  # Output: Alice 30 5
