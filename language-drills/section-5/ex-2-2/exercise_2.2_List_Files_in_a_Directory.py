"""
List Files in a Directory

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from pathlib import Path

# List all Python files in the current directory
path = Path(".")
python_files = path.glob("*.py")

# Print all the Python files
for file in python_files:
    print(file.name)
