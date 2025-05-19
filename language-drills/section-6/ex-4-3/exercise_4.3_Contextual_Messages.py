"""
Contextual Messages

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("context_demo")

class User:
    def __init__(self, name):
        self.name = name

user = User("Alice")
logger.debug(f"User: {user.name}")
