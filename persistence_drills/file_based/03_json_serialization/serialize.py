"""Module: serialize.py
Author: Anurag"""

"""
Task 3: JSON Serialization

Author: Anurag
Date: 2024-05-12
Description: Convert a Book object to a JSON string
"""

from book import Book

# Create Book instance
book = Book("Atomic Habits", "James Clear", 2018)

# Serialize to JSON
json_string = book.to_json()

# Save to file (optional)
with open("book.json", "w") as f:
    f.write(json_string)

# Print JSON
print("✅ Book serialized to JSON:")
print(json_string)
