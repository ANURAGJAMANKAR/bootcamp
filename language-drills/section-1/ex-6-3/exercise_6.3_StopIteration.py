"""
StopIteration

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Demonstrates raising StopIteration manually
and catching it in a loop.
"""

def manual_iter():
    yield 1
    raise StopIteration("Done")

gen = manual_iter()

try:
    print(next(gen))  # 1
    print(next(gen))  # Raises StopIteration
except StopIteration as e:
    print("Caught StopIteration:", e)
