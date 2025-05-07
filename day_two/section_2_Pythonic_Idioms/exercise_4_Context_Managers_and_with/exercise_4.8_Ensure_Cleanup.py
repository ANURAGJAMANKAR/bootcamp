"""
Ensure Cleanup

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrate how a context manager always exits, even on error.
Helps ensure resources are released.
"""

class SafeContext:
    def __enter__(self):
        print("🚪 Entered safely")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("🧹 Cleanup triggered!")
        if exc_type:
            print(f"⚠️ Error caught: {exc_val}")
        return False  # re-raise exception if any

with SafeContext():
    print("...about to do something risky...")
    raise ValueError("Boom! Something went wrong!")
