"""
Rotate a Deque

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from collections import deque

# Create a deque
dq = deque([1, 2, 3, 4, 5])

# Rotate the deque by 2 positions
dq.rotate(2)

# Print the result
print(dq)


""" 

Output:
deque([4, 5, 1, 2, 3])


"""