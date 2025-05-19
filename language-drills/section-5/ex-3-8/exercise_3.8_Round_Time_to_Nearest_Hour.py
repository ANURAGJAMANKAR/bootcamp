"""
Round Time to Nearest Hour

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from datetime import datetime

# Get the current time
now = datetime.now()

# Round to the top of the hour
rounded_time = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)

# Print the rounded time
print(f"Rounded Time to the Nearest Hour: {rounded_time}")
