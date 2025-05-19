"""
Fail Loud Then Gracefully

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_data(data):
    try:
        if data == "fail":
            raise ValueError("Data is invalid")
        return f"Processed {data}"
    except ValueError as e:
        logger.error(f"Error occurred: {e}")
        raise  # Reraise the exception after logging it

try:
    process_data("fail")
except ValueError:
    pass  # Handle the exception after it's logged
