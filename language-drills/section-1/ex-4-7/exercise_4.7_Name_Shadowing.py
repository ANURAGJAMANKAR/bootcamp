"""
Name Shadowing

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrates what happens when a built-in name like 'len'
is shadowed by a variable. Spoiler: it breaks stuff.
"""

len = 5  # Shadowing built-in len()

# This will raise a TypeError
try:
    print(len(["a", "b"]))  # TypeError: 'int' object is not callable
except TypeError as e:
    print("Oops, shadowed built-in:", e)

# Fix it by deleting your override
del len
print("Now len(['a','b']):", len(["a", "b"]))  # Works again
