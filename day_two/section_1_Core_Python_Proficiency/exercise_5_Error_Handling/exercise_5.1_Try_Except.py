"""
Try Except

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This snippet catches a division by zero error
and prints a graceful message instead of crashing.
"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide")
