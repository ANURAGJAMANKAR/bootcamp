"""
Avoid Temporary Lists

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

# Use generator expression to avoid creating an intermediate list
result = sum(x for x in range(1000000))  # More memory efficient
print(f"Sum: {result}")
