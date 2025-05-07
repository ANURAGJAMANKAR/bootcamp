"""
Use Itertools Islice

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import itertools

def read_first_10_lines(file_path):
    """Read the first 10 lines of a file using islice."""
    with open(file_path, 'r') as file:
        return list(itertools.islice(file, 10))

# Example usage
file_path = 'large_file.txt'
first_10_lines = read_first_10_lines(file_path)
print(first_10_lines)
