"""
Use Str for Printing

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Define __str__ in Book for clean print output.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("To Kill a Mockingbird", "Harper Lee")
print(book)  # Calls __str__ implicitly
