"""
Multiple Exceptions

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Catches and handles multiple exception types separately.
"""

try:
    num = int("oops")  # ValueError
    result = 10 / num  # ZeroDivisionError if num is 0
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
