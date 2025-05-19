"""
Conditional Logging

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

debug = True  # Set to False to suppress debug messages

logging.basicConfig(
    level=logging.DEBUG if debug else logging.INFO,
    format='%(levelname)s — %(message)s'
)
logger = logging.getLogger("conditional_logger")

logger.debug("This debug message shows only if debug=True")
logger.info("This always shows if level is INFO or lower")
