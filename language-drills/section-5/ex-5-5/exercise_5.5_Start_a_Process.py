"""
Start a Process

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import multiprocessing
import time

# Function to run in a process
def compute_square(number):
    time.sleep(2)
    print(f"Square of {number} is {number * number}")

# Start a process
process = multiprocessing.Process(target=compute_square, args=(5,))
process.start()

# Wait for the process to finish
process.join()
