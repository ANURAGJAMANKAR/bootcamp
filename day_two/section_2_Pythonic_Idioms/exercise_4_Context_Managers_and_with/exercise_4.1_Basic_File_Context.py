"""
Basic File Context

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Open a file and read its contents using a context manager.
This ensures the file is closed properly after use.
"""

with open("example.txt", "r") as f:
    content = f.read()
    print(content)
