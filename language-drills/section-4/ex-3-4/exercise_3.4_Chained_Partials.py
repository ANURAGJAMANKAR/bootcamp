"""
Chained Partials

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import functools

# Start with a partial function to print a message
print_message = functools.partial(print, "Message:")

# Chain another partial to add a specific prefix
custom_print = functools.partial(print_message, "Custom Prefix")

# Test the chained partials
custom_print("Hello World!")  # Prints: Message: Custom Prefix Hello World!
