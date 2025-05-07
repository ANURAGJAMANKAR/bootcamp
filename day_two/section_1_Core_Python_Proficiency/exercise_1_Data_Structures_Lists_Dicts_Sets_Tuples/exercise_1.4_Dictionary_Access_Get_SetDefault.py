"""
Dictionary Access Get SetDefault

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script demonstrates how to access dictionary values using `.get()` 
and how to add default values using `.setdefault()`.
"""

user = {"name": "Alice"}

# Access 'name' safely using .get()
print("Name (get):", user.get("name"))

# Access a non-existent key with .get(), returns None
print("Age (get):", user.get("age"))

# Add 'age' if not present using setdefault()
user.setdefault("age", 25)

print("User dictionary after setdefault:", user)
