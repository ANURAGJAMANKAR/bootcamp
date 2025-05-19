"""
Suppress Print Statements

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("suppress_print")

# Instead of print("Starting script...")
logger.info("Starting script...")

# Instead of print("Processing complete.")
logger.info("Processing complete.")
