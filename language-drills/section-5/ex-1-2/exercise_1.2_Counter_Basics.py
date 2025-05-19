"""
Counter Basics

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from collections import Counter

# Count character frequencies in "hello world"
text = "hello world"
char_count = Counter(text)

# Print the frequencies of each character
print(char_count)


""" 

OUTPUT:
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


"""