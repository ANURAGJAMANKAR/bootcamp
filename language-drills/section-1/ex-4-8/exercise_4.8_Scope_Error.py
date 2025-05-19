"""
Scope Error

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Shows an UnboundLocalError by referencing a variable
before it's assigned locally inside a function.
"""

def broken():
    try:
        print(x)  # Tries to read before local assignment
        x = 10    # Local assignment happens too late
    except UnboundLocalError as e:
        print("Scope error:", e)

broken()
