"""
Str vs Repr

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrate the difference between __str__ and __repr__.
__str__ is for user-friendly string representation,
__repr__ is for developer-friendly string representation (e.g., debugging).
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book = Book("1984", "George Orwell")

# Print calls __str__, while repr can be checked in the debugger or explicitly.
print(book)  # Calls __str__
print(repr(book))  # Calls __repr__
