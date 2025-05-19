"""
Filter with Comprehension

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script uses a list comprehension to filter strings with even lengths.
"""

words = ["hi", "hello", "bye"]

# Only include strings with even length
even_length_words = [word for word in words if len(word) % 2 == 0]

print("Even-length words:", even_length_words)  # Output: ['hi']
