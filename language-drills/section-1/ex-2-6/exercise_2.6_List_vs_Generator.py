"""
List vs Generator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This script compares memory usage between a list comprehension and 
a generator expression that both produce 1 million numbers.
"""

import sys

list_comp = [x for x in range(1000000)]  # Eagerly loads all data into memory
gen_exp = (x for x in range(1000000))    # Generates items on the fly

print("List comprehension size:", sys.getsizeof(list_comp), "bytes")
print("Generator expression size:", sys.getsizeof(gen_exp), "bytes")

# Output will show that the generator is WAY more memory efficient
