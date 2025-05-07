"""
Short Circuiting with Any

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

numbers = [10, 20, 30, 99, 40, 50, 60]

# Check if any number in the list is divisible by 99 using any()
result = any(x % 99 == 0 for x in numbers)
print(f"Is any number divisible by 99? {result}")
