"""
Secure Unpickling

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import json

# Example object
data = {"name": "Alice", "age": 25}

# Serialize to JSON (Safe)
with open('data.json', 'w') as file:
    json.dump(data, file)

# Deserialize back from JSON
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(f"Loaded Data from JSON: {loaded_data}")
