"""
Debug Recursive Calls

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def recursive_function(n, level=0):
    logger.debug(f"{' ' * level}Entering recursive function with n={n}, level={level}")
    if n > 0:
        recursive_function(n - 1, level + 1)
    logger.debug(f"{' ' * level}Exiting recursive function with n={n}, level={level}")

recursive_function(3)
