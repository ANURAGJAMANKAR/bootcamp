"""
Parse Date String

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from datetime import datetime

# Parse a date string into a datetime object
date_string = "2024-01-01"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")

# Print the parsed date
print(f"Parsed Date: {parsed_date}")
