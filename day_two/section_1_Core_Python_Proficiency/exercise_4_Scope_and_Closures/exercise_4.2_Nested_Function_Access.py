"""
Nested Function Access

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Inner function accessing a variable from the outer function (enclosing scope).
"""

def outer():
    msg = "Hello from outer"

    def inner():
        print(msg)  # Can access 'msg' from outer scope

    inner()

outer()
