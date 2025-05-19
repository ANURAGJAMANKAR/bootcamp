"""
Nonlocal

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Uses 'nonlocal' to modify a variable in the enclosing function's scope.
"""

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("Inner count:", count)

    inner()
    print("Outer count after inner:", count)

outer()
