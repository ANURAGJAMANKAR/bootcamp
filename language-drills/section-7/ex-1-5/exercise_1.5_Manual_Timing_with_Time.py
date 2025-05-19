"""
Manual Timing with Time

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import time

start_time = time.time()
# Your function call or code to measure
result = sum(range(10000))
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")
