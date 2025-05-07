"""
Add Error IDs

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_data():
    """Function that simulates an error."""
    try:
        raise ValueError("Invalid input data")
    except Exception as e:
        error_id = 12345  # Example error ID
        logger.error(f"Error ID: {error_id}, Error: {str(e)}")

process_data()
