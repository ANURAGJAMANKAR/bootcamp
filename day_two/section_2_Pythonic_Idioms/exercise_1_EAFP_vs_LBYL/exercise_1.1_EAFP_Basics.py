"""
EAFP Basics

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
EAFP-style dict access: Try accessing a key directly,
catch KeyError if it's missing.
"""

data = {"name": "Anurag"}

try:
    print(data["age"])
except KeyError:
    print("Key 'age' not found")
