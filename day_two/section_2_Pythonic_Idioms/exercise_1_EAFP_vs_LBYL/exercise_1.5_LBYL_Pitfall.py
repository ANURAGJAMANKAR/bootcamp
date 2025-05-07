"""
LBYL Pitfall

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Shows how LBYL can be dangerous when checking for file existence
before opening it (race condition possibility).
"""

import os

filename = "tempfile.txt"

if os.path.exists(filename):  # LBYL: File exists?
    # Problem: file might be deleted after this check
    with open(filename) as f:
        print(f.read())
else:
    print("File does not exist")
