"""
Callability

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Implement __call__ to make an instance of Greeter callable like a function.
"""

class Greeter:
    def __call__(self, name):
        return f"Hello, {name}!"

greeter = Greeter()
print(greeter("Anurag"))  # Calls __call__ method, should print "Hello, Anurag!"
