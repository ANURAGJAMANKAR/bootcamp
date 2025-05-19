"""
Deque for Stack and Queue

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from collections import deque

# Create a deque for a stack (LIFO)
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack:", stack)

# Pop an item from the stack
stack.pop()
print("Stack after pop:", stack)

# Create a deque for a queue (FIFO)
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue:", queue)

# Pop an item from the queue
queue.popleft()
print("Queue after popleft:", queue)



""" 

OUTPUT
Stack: deque([1, 2, 3])
Stack after pop: deque([1, 2])
Queue: deque([1, 2, 3])
Queue after popleft: deque([2, 3])


"""