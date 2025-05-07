"""
Class vs Instance Variable

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrate class variable vs instance variable.
"""

class Book:
    category = "Fiction"  # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author

book3 = Book("Fahrenheit 451", "Ray Bradbury")
print(f"Category: {book3.category}")
