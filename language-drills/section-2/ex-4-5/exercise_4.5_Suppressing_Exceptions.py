"""
Suppressing Exceptions

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Use contextlib.suppress to ignore specific exceptions.
Here, we ignore FileNotFoundError.
"""

from contextlib import suppress

with suppress(FileNotFoundError):
    with open("nonexistent_file.txt") as f:
        print(f.read())
