"""
Hashing Support

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Add __hash__ to make Book objects usable in a set or as dictionary keys.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Brave New World", "Aldous Huxley")

books_set = {book1, book2, book3}  # Set of books
print(books_set)  # book1 and book2 should be considered equal, so only one will appear
