"""
Simple Generator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
A generator function that counts down from n to 1.
"""

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)  # 3 2 1
