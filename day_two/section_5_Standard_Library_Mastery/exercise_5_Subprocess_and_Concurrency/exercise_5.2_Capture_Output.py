"""
Capture Output

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import subprocess

# Capture the output of 'ls' command
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(f"Command Output:\n{result.stdout}")
print(f"Error Output (if any):\n{result.stderr}")
