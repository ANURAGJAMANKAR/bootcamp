"""
Use Pdb Set Trace

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import pdb

def sample_function(a, b):
    result = a + b
    pdb.set_trace()  # Pauses execution here and enters interactive debugging
    return result

sample_function(2, 3)
