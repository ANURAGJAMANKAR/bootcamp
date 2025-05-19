"""
Add New Attribute

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Add a new attribute `genre` to Novel and test it.
"""

class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

novel = Novel("Frankenstein", "Mary Shelley", "Gothic Horror")
print(f"{novel.describe()} | Genre: {novel.genre}")
