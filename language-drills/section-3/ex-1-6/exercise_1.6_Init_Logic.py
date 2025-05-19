"""
Init Logic

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Provide default values in the constructor for flexibility.
"""

class Book:
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

default_book = Book()
custom_book = Book("Dune", "Frank Herbert")

print(default_book.describe())
print(custom_book.describe())
