"""
Use Timeit

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import timeit

# Time the execution of sum(range(10000))
execution_time = timeit.timeit("sum(range(10000))", number=1000)
print(f"Execution time: {execution_time:.6f} seconds")
