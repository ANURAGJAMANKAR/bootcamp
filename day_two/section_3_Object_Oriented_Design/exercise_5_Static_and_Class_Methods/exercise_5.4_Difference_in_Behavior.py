"""
Difference in Behavior

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrating that static methods don't have access to cls or self.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def print_title():
        # This will raise an error because static methods don't have access to self
        # print(self.title)  # Uncommenting this will raise an error
        print("This is a static method, no access to 'self' or 'cls'.")

book = Book("1984", "George Orwell")
book.print_title()  # Output: This is a static method, no access to 'self' or 'cls'.
