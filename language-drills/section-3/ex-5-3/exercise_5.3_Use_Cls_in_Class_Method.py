"""
Use Cls in Class Method

Instructions:
Complete the exercise according to the requirements.
"""
# Author: Anurag

"""
Class method returning instances of the class it's called on, even with subclasses.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, s: str):
        title, author = s.split("|")
        return cls(title, author)

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    @classmethod
    def from_string(cls, s: str):
        title, author, file_size = s.split("|")
        book = super().from_string(f"{title}|{author}")
        book.file_size = int(file_size)  # Adding file size for EBook
        return book

# Testing subclass with class method
ebook_str = "Digital Fortress|Dan Brown|500"
ebook_from_str = EBook.from_string(ebook_str)
print(ebook_from_str.title)  # Output: Digital Fortress
print(ebook_from_str.author)  # Output: Dan Brown
print(ebook_from_str.file_size)  # Output: 500
