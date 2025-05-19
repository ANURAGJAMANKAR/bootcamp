"""
Multiple Contexts

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Open two files simultaneously using a single with statement.
Useful for copying or comparing file contents.
"""

with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
    data = fin.read()
    fout.write(data)
