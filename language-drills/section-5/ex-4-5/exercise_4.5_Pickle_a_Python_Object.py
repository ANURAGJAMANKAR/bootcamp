"""
Pickle a Python Object

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import pickle

# Example object
data = {"name": "Alice", "age": 25}

# Serialize with pickle
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Deserialize with pickle
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)
    print(f"Unpickled Data: {loaded_data}")
