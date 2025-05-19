"""
Database Style Locking

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Simulate a database-style resource lock using __enter__ and __exit__.
Prints connection status on entry and cleanup on exit.
"""

class DBConnection:
    def __enter__(self):
        print("🔒 Connecting to database...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("🔓 Closing database connection...")

with DBConnection():
    print("...running DB queries...")
