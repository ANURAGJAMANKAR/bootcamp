"""
Copy Files with Shutil

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import shutil
from pathlib import Path

# Define source and destination paths
source_file = Path("source.txt")
destination_file = Path("destination.txt")

# Copy file from source to destination
shutil.copy(source_file, destination_file)

# Verify file copy
print(f"File copied to: {destination_file}")
