"""
Boolean Check

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Implement __bool__ to define when an object is considered True or False.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __bool__(self):
        return bool(self.title)  # If there's a title, it's "truthy"

book1 = Book("1984", "George Orwell")
book2 = Book("", "Unknown")

print(bool(book1))  # Should print True (non-empty title)
print(bool(book2))  # Should print False (empty title)
