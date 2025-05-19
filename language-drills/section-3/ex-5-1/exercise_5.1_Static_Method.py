"""
Static Method

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Static method to validate if a string is a valid ISBN.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        # A very basic check for ISBN format (length 10 or 13, numeric characters only)
        return len(isbn) in [10, 13] and isbn.isdigit()

# Testing static method
print(Book.is_valid_isbn("1234567890"))  # Output: True
print(Book.is_valid_isbn("9781234567890"))  # Output: True
print(Book.is_valid_isbn("abc123"))  # Output: False
