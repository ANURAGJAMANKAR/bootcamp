"""
Suppressing Exceptions

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Uses contextlib.suppress to gracefully ignore a KeyError.
"""

from contextlib import suppress

my_dict = {"name": "Anurag"}

with suppress(KeyError):
    print(my_dict["age"])  # This will be silently ignored
