"""
Run a Command

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import subprocess

# Running the 'ls -l' command (Linux/macOS equivalent, or 'dir' for Windows)
subprocess.run(["ls", "-l"])  # For Linux/macOS
# For Windows, you can use subprocess.run(["dir"], shell=True)
