"""
Subclassing

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Create a Novel class that inherits from the Book class.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Novel(Book):
    pass  # Inherits everything from Book for now
