"""
Use Concurrent Futures

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from concurrent.futures import ThreadPoolExecutor
import time

# Function to run in threads
def task(n):
    time.sleep(1)
    return f"Task {n} completed"

# Use ThreadPoolExecutor to parallelize the execution
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))

for result in results:
    print(result)
