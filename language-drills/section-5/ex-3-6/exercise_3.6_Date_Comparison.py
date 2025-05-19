"""
Date Comparison

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from datetime import datetime

# Define two dates
date1 = datetime(2024, 5, 1)
date2 = datetime(2025, 1, 1)

# Compare the dates
if date1 < date2:
    print(f"{date1} is earlier than {date2}")
elif date1 > date2:
    print(f"{date1} is later than {date2}")
else:
    print(f"{date1} and {date2} are the same")
