"""
Send to Generator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
A generator that accepts input using .send() and processes it.
"""

def echo():
    while True:
        received = yield
        print("Received:", received)

gen = echo()
next(gen)           # Prime the generator
gen.send("Hello")   # Output: Received: Hello
