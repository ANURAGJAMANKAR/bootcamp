"""
Time Delta Arithmetic

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
from datetime import datetime, timedelta

# Current date
today = datetime.now()

# Add 7 days to today
future_date = today + timedelta(days=7)

# Print the future date
print(f"Date after 7 days: {future_date}")
