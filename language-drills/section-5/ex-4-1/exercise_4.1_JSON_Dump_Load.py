"""
JSON Dump Load

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import json

# Example dictionary
data = {"name": "Alice", "age": 25}

# Serialize to JSON string
json_data = json.dumps(data)
print(f"Serialized JSON: {json_data}")

# Deserialize back to Python dictionary
loaded_data = json.loads(json_data)
print(f"Deserialized Python Object: {loaded_data}")
