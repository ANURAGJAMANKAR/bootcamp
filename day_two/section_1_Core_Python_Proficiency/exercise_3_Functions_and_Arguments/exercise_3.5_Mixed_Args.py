"""
Mixed Args

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This function accepts both variable positional and keyword arguments.
It prints both for demonstration.
"""

def mix_args(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

mix_args(1, 2, 3, mode="debug", retries=2)
