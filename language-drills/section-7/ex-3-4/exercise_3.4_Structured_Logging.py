"""
Structured Logging

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug("Entering process_data function")
    result = data * 2
    logger.debug("Exiting process_data function")
    return result

process_data(10)
