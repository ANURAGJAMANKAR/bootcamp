"""
Absolute vs Relative Paths

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from pathlib import Path

# Define a relative path
relative_path = Path("myfile.txt")

# Get the absolute path using resolve()
absolute_path = relative_path.resolve()

# Print the absolute path
print(f"Absolute path: {absolute_path}")
