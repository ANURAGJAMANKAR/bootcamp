#!/usr/bin/env python3
# Level 0: Basic Script (No Abstraction)
# This script reads stdin line by line, strips whitespace, converts to uppercase, and prints to stdout.

import sys

# Read from stdin line by line
for line in sys.stdin:
    # Strip leading and trailing whitespace
    stripped_line = line.strip()
    
    # Convert to uppercase
    uppercase_line = stripped_line.upper()
    
    # Print to stdout
    print(uppercase_line)
