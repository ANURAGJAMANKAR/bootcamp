"""
Reraise Exception

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Logs an exception and then re-raises it for higher-level handling.
"""

try:
    raise ValueError("Something went wrong")
except ValueError as e:
    print("Logging error:", e)
    raise  # Reraises the same error
