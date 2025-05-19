"""
Use Inline Comments Sparingly

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

def retry_login():
    """Retry login due to flaky authentication backend."""
    for _ in range(3):
        if login():  # Retry because login fails intermittently
            return True
    return False
