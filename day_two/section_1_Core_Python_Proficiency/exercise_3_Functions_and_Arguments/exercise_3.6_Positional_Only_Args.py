"""
Positional Only Args

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This function demonstrates the use of positional-only arguments.
Arguments before `/` must be passed positionally.
"""

def divide(a, b, /):
    return a / b

# These work:
print(divide(10, 2))

# This will raise an error:
# divide(a=10, b=2)
