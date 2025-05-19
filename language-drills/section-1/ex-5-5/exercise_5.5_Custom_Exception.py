"""
Custom Exception

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Defines a custom exception for invalid age input.
Raises it if the age is negative.
"""

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    else:
        print("Age is valid.")

try:
    check_age(-5)
except InvalidAgeError as e:
    print("Caught custom exception:", e)
