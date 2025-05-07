"""
Closure Memory

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Uses a closure created from make_multiplier to multiply values.
Demonstrates memory of enclosed variable 'n'.
"""

triple = make_multiplier(3)

print("Triple of 10:", triple(10))  # Output: 30
