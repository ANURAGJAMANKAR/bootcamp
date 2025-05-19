"""
Large Data with Generators

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

def read_large_file(file_path):
    """Generator to read a large file line by line."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Example usage
file_path = 'large_file.txt'
for line in read_large_file(file_path):
    print(line)
