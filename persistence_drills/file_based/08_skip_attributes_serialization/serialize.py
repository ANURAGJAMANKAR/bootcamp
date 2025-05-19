"""Module: serialize.py
Author: Anurag"""

"""
Task 8: Skipping Attributes During Serialization

Author: Anurag
Date: 2024-05-12
Description: Serialize a User object while excluding sensitive attributes
"""

import json
import os
import hashlib
from typing import Dict, Any, Optional

from user import User

user = User("anurag", "supersecret123", "anurag@example.com")

# Serialize without password
safe_json = user.to_safe_json()

# Save to file
with open("user_safe.json", "w") as f:
    f.write(safe_json)

print("✅ User serialized without sensitive attributes:")
print(safe_json)
