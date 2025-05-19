"""
Global

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrates how to modify a global variable inside a function using 'global'.
"""

x = 10  # Global variable

def modify_global():
    global x
    x = 42
    print("Inside function, x:", x)

modify_global()
print("Outside function, global x:", x)  # x has been modified
