"""
Class Method Decorator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def validate_args(func):
    """A decorator that checks and validates arguments for class methods."""
    def wrapper(self, *args, **kwargs):
        if not args or not isinstance(args[0], int):
            print("Invalid argument! First argument must be an integer.")
            return None
        return func(self, *args, **kwargs)
    return wrapper

# Test validate_args
class MyClass:
    @validate_args
    def set_value(self, value):
        """Sets the value."""
        self.value = value
        print(f"Value set to {value}")

obj = MyClass()
obj.set_value(10)  # Valid
obj.set_value("abc")  # Invalid
