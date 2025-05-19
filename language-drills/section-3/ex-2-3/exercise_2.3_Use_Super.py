"""
Use Super

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Call the parent class's describe() using super() inside the overridden method.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

class Novel(Book):
    def describe(self):
        return "Novel: " + super().describe()

novel = Novel("The Great Gatsby", "F. Scott Fitzgerald")
print(novel.describe())
