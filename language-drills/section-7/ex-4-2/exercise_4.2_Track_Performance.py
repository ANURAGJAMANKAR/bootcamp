"""
Track Performance

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging
import time

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def track_performance():
    """Function to track performance by logging execution time."""
    start_time = time.time()
    
    # Simulate a slow task
    time.sleep(2)
    
    execution_time = time.time() - start_time
    logger.debug(f"Function execution time: {execution_time:.4f} seconds")

track_performance()
