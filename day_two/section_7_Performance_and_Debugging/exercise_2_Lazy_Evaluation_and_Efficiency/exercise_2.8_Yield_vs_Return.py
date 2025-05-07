"""
Yield vs Return

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

def generate_numbers(limit):
    """Generate numbers up to a given limit."""
    for i in range(limit):
        yield i  # Lazy generation of numbers

# Compare with a function that appends to a list (using return)
def generate_numbers_return(limit):
    """Generate numbers up to a given limit (returns a list)."""
    numbers = []
    for i in range(limit):
        numbers.append(i)
    return numbers

# Example usage
gen = generate_numbers(5)
print(list(gen))  # Using the generator (one-by-one generation)
