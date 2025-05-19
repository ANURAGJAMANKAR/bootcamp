"""
Nested Try Blocks

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrates nested try blocks and handling different exceptions
at each level.
"""

try:
    print("Outer try")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Handled division by zero in inner try")
    x = int("not a number")
except ValueError:
    print("Handled invalid int in outer try")
