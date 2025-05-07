"""
Use Logging Levels

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("level_demo")

logger.debug("Debugging info")
logger.info("Informational message")
logger.warning("This is a warning")
logger.error("An error occurred")
logger.critical("Critical issue")
