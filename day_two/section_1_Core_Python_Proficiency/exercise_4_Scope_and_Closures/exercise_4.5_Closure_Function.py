"""
Closure Function

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Creates a closure using an outer function that returns an inner function.
The inner function retains access to the outer variable 'n'.
"""

def make_multiplier(n):
    def multiplier(x):
        return n * x
    return multiplier

# Create a triple function
triple = make_multiplier(3)
