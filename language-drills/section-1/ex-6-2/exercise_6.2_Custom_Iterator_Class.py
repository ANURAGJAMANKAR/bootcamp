"""
Custom Iterator Class

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
A simple iterator class that counts up to a given number.
Implements __iter__ and __next__ methods.
"""

class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for num in Counter(3):
    print(num)  # 1 2 3
