"""
Ordering Support

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Implement __lt__ to enable sorting books by their title.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __lt__(self, other):
        return self.title < other.title

book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

books = [book1, book2, book3]
books.sort()  # Sorts by title
for book in books:
    print(book.title)  # Will print sorted titles
