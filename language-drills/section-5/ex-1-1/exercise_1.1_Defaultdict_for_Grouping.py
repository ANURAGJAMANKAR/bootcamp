"""
Defaultdict for Grouping

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from collections import defaultdict

# Group words by their first letter
words = ["apple", "banana", "cherry", "apricot", "blueberry"]
grouped_by_first_letter = defaultdict(list)

for word in words:
    grouped_by_first_letter[word[0]].append(word)

# Print the grouped words
for key, group in grouped_by_first_letter.items():
    print(f"{key}: {group}")


"""

OUTPUT:
a: ['apple', 'apricot']
b: ['banana', 'blueberry']
c: ['cherry']

"""