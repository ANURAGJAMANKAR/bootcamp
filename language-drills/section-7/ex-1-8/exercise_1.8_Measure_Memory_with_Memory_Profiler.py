"""
Measure Memory with Memory Profiler

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

# Install memory_profiler if not already installed:
# pip install memory_profiler

from memory_profiler import profile

@profile
def memory_intensive_function():
    lst = [i * 2 for i in range(1000000)]
    return sum(lst)

if __name__ == "__main__":
    memory_intensive_function()

# To profile memory usage, run the script with:
# python -m memory_profiler yourscript.py
