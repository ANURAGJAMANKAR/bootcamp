"""
Variable Keyword Args

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This function accepts any number of keyword arguments
and prints each key-value pair using **kwargs.
"""

def show_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_settings(theme="dark", autosave=True, volume=75)
