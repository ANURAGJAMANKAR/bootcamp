"""
Safe Type Conversion EAFP

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Attempts to convert a string to an integer using EAFP.
Handles ValueError if conversion fails.
"""

value = "123abc"

try:
    number = int(value)
    print("Converted:", number)
except ValueError:
    print("Invalid integer format")
