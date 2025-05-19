"""
Generator Expression Filter

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Filters even numbers from a range using a generator expression.
"""

evens = (x for x in range(10) if x % 2 == 0)
for num in evens:
    print(num)  # 0 2 4 6 8
