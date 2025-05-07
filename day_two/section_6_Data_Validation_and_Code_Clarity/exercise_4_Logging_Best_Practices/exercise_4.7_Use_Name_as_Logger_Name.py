"""
Use Name as Logger Name

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info("This logger is named after the module.")

"""
Why use __name__?
------------------
Using `__name__` ensures that:
1. The logger is uniquely named per module.
2. It helps trace logs to their source module in large applications.
3. Only the main script configures logging—imported modules won't reconfigure it.
"""
