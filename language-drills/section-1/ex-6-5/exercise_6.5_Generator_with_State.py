"""
Generator with State

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Yields running totals from a list of numbers.
"""

def running_total(nums):
    total = 0
    for n in nums:
        total += n
        yield total

for val in running_total([1, 2, 3]):
    print(val)  # 1 3 6
