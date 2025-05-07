"""
Update Object State

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Add a method to update the book's title.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def update_title(self, new_title):
        self.title = new_title

book4 = Book("Old Title", "Someone")
book4.update_title("New Title")
print(book4.title)
