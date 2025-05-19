"""
When to Prefer LBYL

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Uses isinstance to avoid applying incompatible methods on objects.
An example of when LBYL is safer.
"""

def reverse_string(s):
    if isinstance(s, str):  # LBYL wins here
        return s[::-1]
    else:
        return "Not a string"

print(reverse_string("hello"))  # 'olleh'
print(reverse_string(123))      # 'Not a string'
