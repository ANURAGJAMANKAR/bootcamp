"""
Temporary File

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Use tempfile.TemporaryFile to create a temporary file.
It's deleted automatically when closed.
"""

import tempfile

with tempfile.TemporaryFile(mode="w+t") as temp:
    temp.write("Some temp data")
    temp.seek(0)
    print(temp.read())
