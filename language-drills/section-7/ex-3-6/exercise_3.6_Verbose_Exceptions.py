"""
Verbose Exceptions

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

def handle_exception():
    try:
        result = 1 / 0  # Division by zero error
    except Exception as e:
        print(f"Exception Type: {type(e)}")
        print(f"Exception Message: {e}")

handle_exception()
