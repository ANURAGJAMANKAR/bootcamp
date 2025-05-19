"""
Set Comprehension

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script extracts all unique vowels from the string 'hello world'
using set comprehension.
"""

text = "hello world"
vowels = "aeiou"

# Grab unique vowels from text
unique_vowels = {ch for ch in text if ch in vowels}

print("Unique vowels:", unique_vowels)  # Output might be: {'o', 'e'}
