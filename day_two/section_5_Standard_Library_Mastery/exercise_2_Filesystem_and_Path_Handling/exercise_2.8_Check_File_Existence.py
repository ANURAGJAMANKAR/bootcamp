"""
Check File Existence

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from pathlib import Path

# Define a file path
file_path = Path("myfile.txt")

# Check if the file exists and if it's a file
if file_path.exists():
    print(f"File exists: {file_path.exists()}")
    if file_path.is_file():
        print(f"{file_path} is a file.")
    else:
        print(f"{file_path} is not a file.")
else:
    print(f"{file_path} does not exist.")
