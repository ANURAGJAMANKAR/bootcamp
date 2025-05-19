"""
Trace Function Calls

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def trace_function_calls(func):
    """Decorator to log function calls."""
    def wrapper(*args, **kwargs):
        logger.debug(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logger.debug(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@trace_function_calls
def add(a, b):
    """Function that adds two numbers."""
    return a + b

add(3, 4)
