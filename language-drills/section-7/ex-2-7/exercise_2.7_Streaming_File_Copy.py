"""
Streaming File Copy

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

def copy_file_line_by_line(src, dest):
    """Copy file line by line to avoid reading the entire file into memory."""
    with open(src, 'r') as infile, open(dest, 'w') as outfile:
        for line in infile:
            outfile.write(line)

# Example usage
src_file = 'source.txt'
dest_file = 'destination.txt'
copy_file_line_by_line(src_file, dest_file)
