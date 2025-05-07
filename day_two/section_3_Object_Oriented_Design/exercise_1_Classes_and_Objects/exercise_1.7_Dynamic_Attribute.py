"""
Dynamic Attribute

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Add an attribute dynamically after object creation.
"""

book5 = Book("The Hobbit", "Tolkien")
book5.year = 1937  # Dynamic attribute addition
print(f"{book5.describe()}, published in {book5.year}")
