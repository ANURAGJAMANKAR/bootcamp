"""
Inline Function Composition

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def compose(f, g):
    return lambda x: f(g(x))

# Test compose with functions
double = lambda x: x * 2
increment = lambda x: x + 1

composed_function = compose(double, increment)
print(composed_function(3))  # Output: 8 (first increment(3) => 4, then double(4) => 8)
