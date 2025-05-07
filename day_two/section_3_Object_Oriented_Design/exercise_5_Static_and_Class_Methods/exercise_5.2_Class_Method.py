"""
Class Method

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Class method to create a Book instance from a string "Title|Author".
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, s: str):
        title, author = s.split("|")
        return cls(title, author)

# Testing class method
book_str = "1984|George Orwell"
book_from_str = Book.from_string(book_str)
print(book_from_str.title)  # Output: 1984
print(book_from_str.author)  # Output: George Orwell
