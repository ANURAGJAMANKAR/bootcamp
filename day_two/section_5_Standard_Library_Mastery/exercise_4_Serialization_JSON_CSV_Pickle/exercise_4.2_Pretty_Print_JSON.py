"""
Pretty Print JSON

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import json

# Example dictionary
data = {"name": "Alice", "age": 25, "location": "Wonderland"}

# Pretty print JSON
pretty_json = json.dumps(data, indent=4, sort_keys=True)
print(f"Pretty Printed JSON:\n{pretty_json}")
