"""
Use Traceback Module

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import traceback

def raise_error():
    try:
        x = 1 / 0  # Division by zero error
    except Exception as e:
        print("Detailed error trace:")
        print(traceback.format_exc())

raise_error()
