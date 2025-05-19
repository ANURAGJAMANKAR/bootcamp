"""
Get Weekday Name

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import calendar
from datetime import datetime

# Get today's date
today = datetime.now()

# Get the weekday name
weekday_name = calendar.day_name[today.weekday()]

# Print the weekday name
print(f"Today is: {weekday_name}")
