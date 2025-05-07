"""
Start a Thread

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import threading
import time

# Function to run in a thread
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# Start a thread
thread = threading.Thread(target=print_numbers)
thread.start()

# Wait for the thread to finish
thread.join()
