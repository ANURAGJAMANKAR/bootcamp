"""
Create and Delete File Directory

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import os
import shutil
from pathlib import Path

# Create a temporary directory
temp_dir = Path("temp_dir")
os.makedirs(temp_dir, exist_ok=True)

# Create a file in the temp directory
temp_file = temp_dir / "temp_file.txt"
temp_file.write_text("This is a temporary file.")

# Verify file creation
print(f"File created: {temp_file.exists()}")

# Delete the directory and its contents
shutil.rmtree(temp_dir)

# Verify deletion
print(f"Directory exists after removal: {temp_dir.exists()}")
