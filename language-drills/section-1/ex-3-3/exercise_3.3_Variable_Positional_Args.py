"""
Variable Positional Args

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This function accepts any number of positional arguments
and returns their total sum using *args.
"""

def add_all(*args):
    return sum(args)

print("Sum:", add_all(1, 2, 3, 4))  # Output: 10
