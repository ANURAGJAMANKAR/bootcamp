"""
OrderedDict Iteration

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3

# Iterate over the ordered dict
for key, value in ordered_dict.items():
    print(key, value)

""" 

OUTPUT
a 1
b 2
c 3


"""