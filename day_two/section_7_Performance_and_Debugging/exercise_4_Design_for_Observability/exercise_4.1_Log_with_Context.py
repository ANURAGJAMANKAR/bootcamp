"""
Log with Context

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging
import inspect

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def log_with_context(user_id):
    """Function to log messages with user ID and function name."""
    function_name = inspect.currentframe().f_code.co_name
    logger.debug(f"User ID: {user_id}, Function: {function_name}, Message: Performing task...")

log_with_context(user_id=123)
