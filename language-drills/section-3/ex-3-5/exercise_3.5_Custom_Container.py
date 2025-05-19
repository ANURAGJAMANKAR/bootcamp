"""
Custom Container

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Implement __len__ to allow len() to work on Library (custom container).
"""

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Brave New World", "Aldous Huxley"))

print(len(library))  # Calls __len__, should return 2
