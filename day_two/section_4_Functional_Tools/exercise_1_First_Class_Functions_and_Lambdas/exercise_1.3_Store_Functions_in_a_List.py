"""
Store Functions in a List

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

funcs = [abs, str, hex]

# Apply each function to -42
result = [func(-42) for func in funcs]
print(result)  # Output: [42, '-42', '-0x2a']
