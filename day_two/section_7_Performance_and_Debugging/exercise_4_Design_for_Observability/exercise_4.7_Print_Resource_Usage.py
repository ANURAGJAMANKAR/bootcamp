"""
Print Resource Usage

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG

import psutil

def print_resource_usage():
    """Print current memory and CPU usage."""
    memory_info = psutil.virtual_memory()
    cpu_usage = psutil.cpu_percent(interval=1)
    
    print(f"Memory Usage: {memory_info.percent}%")
    print(f"CPU Usage: {cpu_usage}%")

print_resource_usage()
