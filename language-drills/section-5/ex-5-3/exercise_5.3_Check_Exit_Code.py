"""
Check Exit Code

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import subprocess

# Run a command and check if it failed
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
if result.returncode != 0:
    print(f"Command failed with error: {result.stderr}")
else:
    print("Command executed successfully!")
