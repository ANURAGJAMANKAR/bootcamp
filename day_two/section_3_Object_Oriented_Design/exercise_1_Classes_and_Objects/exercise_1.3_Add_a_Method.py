"""
Add a Method

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Add a describe method that returns a formatted string with book details.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

book2 = Book("Brave New World", "Aldous Huxley")
print(book2.describe())
