"""
File Handling EAFP

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Opens a file using EAFP-style try/except.
Handles FileNotFoundError if file is missing.
"""

try:
    with open("data.txt") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found")
