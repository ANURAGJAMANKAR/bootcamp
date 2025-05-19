"""
Keyword Arguments

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This function demonstrates keyword arguments.
The function accepts a name and an optional age,
which can be passed in any order using keywords.
"""

def info(name, age=0):
    print(f"Name: {name}, Age: {age}")

# Call with keyword arguments in any order
info(age=25, name="Anurag")
info(name="Zara")
