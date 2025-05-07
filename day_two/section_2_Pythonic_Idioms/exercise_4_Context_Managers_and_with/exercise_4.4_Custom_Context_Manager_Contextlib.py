"""
Custom Context Manager Contextlib

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Use @contextlib.contextmanager to create a timer context.
Prints how long the block took to execute.
"""

import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"⏱️ Took {end - start:.2f} seconds")

with timer():
    time.sleep(1.5)
