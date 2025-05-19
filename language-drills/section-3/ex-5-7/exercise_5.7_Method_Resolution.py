"""
Method Resolution

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Overriding a class method in a subclass and observing the MRO.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def describe(cls):
        print(f"This is a book titled '{cls.title}' by {cls.author}.")

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    @classmethod
    def describe(cls):
        print(f"This is an eBook titled '{cls.title}' by {cls.author} and it is {cls.file_size}MB.")

# Calling the class method from both base and subclass
book = Book("1984", "George Orwell")
ebook = EBook("Brave New World", "Aldous Huxley", 500)

book.describe()  # Output: This is a book titled '1984' by George Orwell.
ebook.describe()  # Output: This is an eBook titled 'Brave New World' by Aldous Huxley and it is 500MB.
