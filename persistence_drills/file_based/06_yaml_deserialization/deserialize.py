"""Module: deserialize.py
Author: Anurag"""

"""
Task 6: YAML Deserialization

Author: Anurag
Date: 2024-05-12
Description: Deserialize a Car object from a YAML string or file
"""

import yaml
from car import Car

# Read YAML from file
with open("car.yaml", "r") as f:
    data = yaml.safe_load(f)

# Reconstruct Car object
car = Car(**data)

# Print details
print("✅ Car object deserialized from YAML:")
print(f"Brand: {car.brand}")
print(f"Model: {car.model}")
print(f"Year: {car.year}")
