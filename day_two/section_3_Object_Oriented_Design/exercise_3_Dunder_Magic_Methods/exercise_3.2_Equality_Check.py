"""
Equality Check

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Implement __eq__ to compare two Book objects by their title and author.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Brave New World", "Aldous Huxley")

print(book1 == book2)  # Should be True
print(book1 == book3)  # Should be False
