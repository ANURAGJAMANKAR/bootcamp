"""
Default Dict Generator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import functools
from collections import defaultdict

# Create a partial function for defaultdict that defaults to an empty list
default_dict_generator = functools.partial(defaultdict, list)

# Test the default dictionary generator
my_dict = default_dict_generator()
my_dict['a'].append(1)
my_dict['b'].append(2)
print(my_dict)  # Should print defaultdict(<class 'list'>, {'a': [1], 'b': [2]})
