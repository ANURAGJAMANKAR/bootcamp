"""
Use Environment Flag for Verbose Mode

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging
import os

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

DEBUG = os.getenv('DEBUG', 'False') == 'True'

def function_to_debug():
    """Function that logs debug information based on environment variable."""
    if DEBUG:
        logger.debug("Debug mode is ON, detailed logs are being generated...")
    else:
        logger.info("Normal mode is ON")

# Set environment variable for testing
os.environ['DEBUG'] = 'True'
function_to_debug()
