"""
Nested Defaultdict

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from collections import defaultdict

# Nested defaultdict
nested_dict = defaultdict(lambda: defaultdict(int))

# Assign values
nested_dict["level1"]["key1"] = 10
nested_dict["level1"]["key2"] = 20
nested_dict["level2"]["key1"] = 30

# Print the result
print(dict(nested_dict))



""" 

OUTPUT:
{'level1': defaultdict(<class 'int'>, {'key1': 10, 'key2': 20}), 'level2': defaultdict(<class 'int'>, {'key1': 30})}


"""