"""
Try Except Else

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Tries to divide two numbers and prints 'Success' only if no exception occurs.
"""

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide")
else:
    print("Success:", result)
