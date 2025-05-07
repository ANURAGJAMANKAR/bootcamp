"""
Polymorphism in Action

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Call describe() on Book and Novel objects in a loop to demonstrate polymorphism.
"""

book1 = Book("Pride and Prejudice", "Jane Austen")
novel1 = Novel("1984", "George Orwell", "Dystopian")

books = [book1, novel1]

for b in books:
    print(b.describe())  # Calls respective describe() method
