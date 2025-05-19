"""
Use Warnings Module

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import warnings

def check_value(value):
    if value < 0:
        warnings.warn("Value is negative, but continuing...", stacklevel=2)

check_value(-1)
