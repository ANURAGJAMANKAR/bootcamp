"""
Benchmark Sorting

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import time

# Built-in sort
start_time = time.time()
sorted_list = sorted(range(1000000))
end_time = time.time()
builtin_sort_time = end_time - start_time
print(f"Built-in sort time: {builtin_sort_time:.6f} seconds")

# Custom sort (e.g., using bubble sort)
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

start_time = time.time()
bubble_sort(list(range(1000000)))
end_time = time.time()
custom_sort_time = end_time - start_time
print(f"Custom sort time: {custom_sort_time:.6f} seconds")
