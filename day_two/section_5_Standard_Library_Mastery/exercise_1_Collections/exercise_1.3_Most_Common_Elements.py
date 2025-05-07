"""
Most Common Elements

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from collections import Counter

# List of numbers
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Get the 2 most common numbers
number_count = Counter(numbers)
most_common_elements = number_count.most_common(2)

# Print the result
print(most_common_elements)


""" 

OUTPUT
[(4, 4), (3, 3)]  # 4 appears 4 times, 3 appears 3 times


"""