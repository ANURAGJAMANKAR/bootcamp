"""
CSV Write

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import csv

# List of dictionaries
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

# Write to CSV file
with open('output.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()  # Write header
    writer.writerows(data)  # Write data rows
