"""
Format Dates

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from datetime import datetime

# Get today's date
today = datetime.now()

# Format the date as "YYYY-MM-DD"
formatted_date = today.strftime("%Y-%m-%d")

# Print the formatted date
print(f"Formatted Date: {formatted_date}")
