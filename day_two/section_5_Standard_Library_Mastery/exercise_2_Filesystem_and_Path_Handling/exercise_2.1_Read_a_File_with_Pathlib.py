"""
Read a File with Pathlib

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from pathlib import Path

# Read the content of "myfile.txt"
file_path = Path("myfile.txt")
content = file_path.read_text()

# Print the content of the file
print(content)
