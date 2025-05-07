"""
Indexing Support

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Implement __getitem__ to allow indexing into a Library object.
"""

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __getitem__(self, index):
        return self.books[index]

library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Brave New World", "Aldous Huxley"))

print(library[0].title)  # Should print "1984"
