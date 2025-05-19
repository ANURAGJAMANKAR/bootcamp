"""
Setup Logger

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

# Set up a basic logger configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("user_logger")

logger.info("Logger initialized successfully.")
