"""
Thread Locking

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import threading

# Shared resource
counter = 0
lock = threading.Lock()

# Function to safely increment the counter
def increment():
    global counter
    with lock:  # Ensure only one thread can access this block at a time
        temp = counter
        temp += 1
        counter = temp

# Start multiple threads
threads = []
for _ in range(5):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
