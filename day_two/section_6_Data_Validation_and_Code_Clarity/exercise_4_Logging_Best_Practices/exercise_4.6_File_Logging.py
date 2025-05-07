"""
File Logging

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

# Log messages will be written to app.log
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s'
)
logger = logging.getLogger("file_logger")

logger.info("This message is logged to a file.")
