"""Module: serialize.py
Author: Anurag"""

"""
Task 1: Basic Serialization with Pickle

Author: Anurag
Date: 2024-05-12
Description: Serialize a Person object to a file using Pickle
"""


import pickle
from person import Person

# Create an instance
person = Person(
    name="Anurag",
    institutions=["Delhi University", "IIT Delhi"],
    colleagues=["Kanan", "Leo"]
)

# Serialize and write to file
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)

print("✅ Person object serialized successfully to 'person.pkl'")
