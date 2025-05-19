"""
Expose Metrics

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging
import time

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

metrics = {
    'function_calls': 0,
    'execution_time': 0.0
}

def function_with_metrics():
    """Function that updates metrics during execution."""
    start_time = time.time()
    metrics['function_calls'] += 1
    
    # Simulate some work
    time.sleep(1)
    
    execution_time = time.time() - start_time
    metrics['execution_time'] += execution_time
    logger.debug(f"Function executed in {execution_time:.4f} seconds")
    logger.info(f"Metrics: {metrics}")

function_with_metrics()
