"""
Conditional Expressions in Comprehensions

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Use conditional expressions inside list comprehensions.
"""

labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']
