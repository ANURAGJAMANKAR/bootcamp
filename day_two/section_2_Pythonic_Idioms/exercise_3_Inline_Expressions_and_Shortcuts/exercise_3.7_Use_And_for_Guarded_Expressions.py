"""
Use And for Guarded Expressions

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
Execute an action only if a condition is True using 'and'.
"""

is_admin = True
user_id = 42

def delete_user(uid):
    print(f"User {uid} deleted.")

is_admin and delete_user(user_id)
