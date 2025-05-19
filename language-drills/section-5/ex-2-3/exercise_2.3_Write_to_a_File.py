"""
Write to a File

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from pathlib import Path

# Write "hello" to a file using pathlib
file_path = Path("hello.txt")
file_path.write_text("hello")

# Alternatively, using open() to write to a file
with open("hello_using_open.txt", "w") as file:
    file.write("hello")
