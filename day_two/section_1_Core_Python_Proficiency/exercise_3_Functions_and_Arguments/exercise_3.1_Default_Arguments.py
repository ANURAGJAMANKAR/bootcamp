"""
Default Arguments

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This function demonstrates the use of default arguments.
If no name is passed, it defaults to 'Guest'.
"""

def greet(name="Guest"):
    print(f"Hello, {name}!")

# Test with and without passing a name
greet()           # Uses default
greet("Anurag")   # Uses given name
