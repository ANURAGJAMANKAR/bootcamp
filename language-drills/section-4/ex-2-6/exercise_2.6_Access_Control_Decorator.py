"""
Access Control Decorator

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

def role_required(role):
    """A decorator that only allows access if the user has the required role."""
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') == role:
                return func(user, *args, **kwargs)
            else:
                print(f"Access denied for user with role {user.get('role')}")
                return None
        return wrapper
    return decorator

# Test role_required
@role_required('admin')
def delete_user(user, user_id):
    """Deletes a user."""
    print(f"User {user_id} deleted by {user['name']}.")

admin_user = {'name': 'Alice', 'role': 'admin'}
regular_user = {'name': 'Bob', 'role': 'user'}

delete_user(admin_user, 123)   # Allowed
delete_user(regular_user, 123)  # Denied
