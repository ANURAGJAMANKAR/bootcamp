"""
Composition of Decorators

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

@simple_logger
@timer
@debug_info
def complex_function(x, y):
    """Performs a complex calculation."""
    return (x + y) * 2

# Test the composition of decorators
complex_function(5, 7)
