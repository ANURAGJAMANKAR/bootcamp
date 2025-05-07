"""
Custom JSON Encoder

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag
import json
from datetime import datetime

# Custom JSON encoder for datetime
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO format
        return super().default(obj)

# Example datetime object
now = datetime.now()

# Serialize with custom encoder
json_data = json.dumps({"current_time": now}, cls=CustomEncoder)
print(f"Serialized datetime: {json_data}")
