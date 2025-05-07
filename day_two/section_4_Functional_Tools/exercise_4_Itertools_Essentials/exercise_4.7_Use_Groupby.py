"""
Use Groupby

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import itertools

# List of dictionaries to be grouped by the 'type' key
items = [
    {"name": "apple", "type": "fruit"},
    {"name": "banana", "type": "fruit"},
    {"name": "carrot", "type": "vegetable"},
    {"name": "broccoli", "type": "vegetable"}
]

# Group the items by 'type' key
items.sort(key=lambda x: x["type"])  # Sort first to make groupby work correctly
grouped_items = itertools.groupby(items, key=lambda x: x["type"])

# Print grouped items
for key, group in grouped_items:
    print(key)  # Prints 'fruit' and 'vegetable'
    for item in group:
        print(item)  # Prints the dictionaries for each type
