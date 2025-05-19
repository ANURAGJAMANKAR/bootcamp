"""
Finally Block

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrates that the finally block always runs,
regardless of whether an exception occurred.
"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide")
finally:
    print("Cleanup done")  # Always prints
