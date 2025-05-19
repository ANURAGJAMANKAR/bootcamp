"""
Defaultdict with Lambda

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from collections import defaultdict

# Create a defaultdict with a lambda returning "N/A"
d = defaultdict(lambda: "N/A")
d["key1"] = "value1"

# Access existing and missing keys
print(d["key1"])  # value1
print(d["key2"])  # N/A (default value)


""" 

OUTPUT
value1
N/A


"""
