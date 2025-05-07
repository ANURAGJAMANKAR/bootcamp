"""
Add Health Check Function

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging
import psutil

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def health_check():
    """Simple function to return system status for debugging."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    logger.info(f"System Health Check: CPU Usage: {cpu_usage}%, Memory Usage: {memory_info.percent}%")

health_check()
