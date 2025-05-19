"""
Invoke Static Method

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Calling static method from both class and instance.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        return len(isbn) in [10, 13] and isbn.isdigit()

# Calling static method via class and instance
print(Book.is_valid_isbn("1234567890"))  # Output: True
book = Book("1984", "Orwell")
print(book.is_valid_isbn("9781234567890"))  # Output: True
