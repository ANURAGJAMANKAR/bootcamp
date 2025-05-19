"""
Format Output

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

# Include timestamp and log level in the format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s'
)
logger = logging.getLogger("formatted_logger")

logger.info("Formatted logging example")
