"""
Kill a Subprocess

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import subprocess
import time

# Start a subprocess (e.g., sleep for 60 seconds)
process = subprocess.Popen(["sleep", "60"])

# Wait for a short period (e.g., 5 seconds) and then terminate it
time.sleep(5)
process.terminate()
print("Subprocess terminated")
