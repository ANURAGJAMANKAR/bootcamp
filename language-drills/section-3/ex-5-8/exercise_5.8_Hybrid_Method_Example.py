"""
Hybrid Method Example

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Hybrid method example where static, class, and instance methods are used together.
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        # Static method to validate ISBN
        return len(isbn) in [10, 13] and isbn.isdigit()

    @classmethod
    def from_string(cls, s: str):
        # Class method to create a book from a string
        title, author, price = s.split("|")
        return cls(title, author, float(price))

    def apply_discount(self, discount: float):
        # Instance method to apply a discount to the price
        self.price -= self.price * discount

# Using all methods
isbn = "1234567890"
book_str = "1984|George Orwell|19.99"

book = Book.from_string(book_str)
print(Book.is_valid_isbn(isbn))  # Static method
book.apply_discount(0.10)  # Instance method to apply discount
print(book.price)  # Output: 17.991
