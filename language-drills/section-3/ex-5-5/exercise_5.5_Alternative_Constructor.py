"""
Alternative Constructor

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Alternative constructors for creating a Book from JSON or dictionary.
"""

import json
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

    @classmethod
    def from_json(cls, json_data: str):
        data = json.loads(json_data)
        return cls(data["title"], data["author"])

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["title"], data["author"])

# Testing alternative constructors
book_json = '{"title": "Brave New World", "author": "Aldous Huxley"}'
book_dict = {"title": "Fahrenheit 451", "author": "Ray Bradbury"}

book_from_json = Book.from_json(book_json)
book_from_dict = Book.from_dict(book_dict)

print(book_from_json)  # Output: Book(title='Brave New World', author='Aldous Huxley')
print(book_from_dict)  # Output: Book(title='Fahrenheit 451', author='Ray Bradbury')
