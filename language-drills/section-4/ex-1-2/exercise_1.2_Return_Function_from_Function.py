"""
Return Function from Function

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def make_doubler():
    return lambda x: x * 2

# Testing make_doubler
doubler = make_doubler()
print(doubler(4))  # Output: 8
