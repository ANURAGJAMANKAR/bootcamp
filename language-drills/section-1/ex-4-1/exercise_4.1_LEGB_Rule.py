"""
LEGB Rule

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrates the LEGB rule by defining a global variable,
then shadowing it with a local one inside a function.
"""

x = 10  # Global variable

def show_scope():
    x = 20  # Local variable shadows the global one
    print("Local x:", x)

show_scope()      # Output: Local x: 20
print("Global x:", x)  # Output: Global x: 10
