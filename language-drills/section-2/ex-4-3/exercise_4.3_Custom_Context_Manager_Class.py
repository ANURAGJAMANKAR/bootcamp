"""
Custom Context Manager Class

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Define a custom context manager using a class with __enter__ and __exit__.
Prints log messages upon entry and exit.
"""

class LoggerContext:
    def __enter__(self):
        print(">> Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("<< Exiting context")

with LoggerContext():
    print("...doing something inside...")
