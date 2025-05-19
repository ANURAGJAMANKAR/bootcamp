"""
Temp File Usage

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import tempfile

# Create a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b"Hello, this is temporary content.")
    print(f"Temporary file created at: {temp_file.name}")
