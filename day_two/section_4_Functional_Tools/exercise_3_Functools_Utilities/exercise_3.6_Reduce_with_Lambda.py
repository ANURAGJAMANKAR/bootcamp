"""
Reduce with Lambda

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from functools import reduce

# Function to compute factorial using reduce
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

# Test the factorial function
print(factorial(5))  # Should print 120
