import json
from datetime import datetime
from app.models.roles import Role
from app.models.user import User, UserSecurity, UserStatus, UserLoginHistory, UserDetails

users = []

def convert_to_serializable(value):
    """Convert non-serializable types (like datetime) into serializable forms."""
    if isinstance(value, datetime):
        return value.isoformat()  # Convert datetime to ISO format string
    elif isinstance(value, Role):
        return value.name  # Convert Role to its name (or another serializable attribute)
    elif isinstance(value, User):
        return value.to_dict()  # Convert User object to dict using to_dict() method
    elif isinstance(value, UserSecurity):
        return value.to_dict()  # Convert UserSecurity to dict
    elif isinstance(value, UserStatus):  
        # Convert all datetime attributes in UserStatus to isoformat
        return value.to_dict()  # Using to_dict() for UserStatus
    elif isinstance(value, UserLoginHistory):  
        # Convert all datetime attributes in UserLoginHistory to isoformat
        return value.to_dict()  # Using to_dict() for UserLoginHistory
    elif isinstance(value, UserDetails):  
        return value.to_dict()  # Using to_dict() for UserDetails
    return value  # If it's not one of the custom objects, just return it as is

class User:
    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'created_at': self.created_at.isoformat(),  # Convert datetime to string
        }

class UserStatus:
    def __init__(self, status, last_updated):
        self.status = status
        self.last_updated = last_updated

    def to_dict(self):
        return {
            'status': self.status,
            'last_updated': self.last_updated.isoformat(),  # Convert datetime to string
        }

class UserLoginHistory:
    def __init__(self, login_time, ip_address):
        self.login_time = login_time
        self.ip_address = ip_address

    def to_dict(self):
        return {
            'login_time': self.login_time.isoformat(),  # Convert datetime to string
            'ip_address': self.ip_address,
        }

class UserDetails:
    def __init__(self, user, security, status, login_history):
        self.user = user
        self.security = security
        self.status = status
        self.login_history = login_history

    def to_dict(self):
        return {
            'user': self.user.to_dict(),  # Convert user to dict
            'security': self.security.to_dict(),  # Convert security to dict
            'status': self.status.to_dict(),  # Convert status to dict
            'login_history': [login.to_dict() for login in self.login_history],  # Convert list of login history
        }

def get_all_users():
    print(f"All users: {users}")

def add_user(user_details: UserDetails):
    users.append(user_details)
    save_users()
    print(f"User {user_details.user.username} added to User DB")

def delete_user(user_details: UserDetails):
    users.remove(user_details)
    print(f"User: {user_details.user.username} deleted from DB.")

def save_users():
    users_data = []
    for user in users:
        # Recursively convert non-serializable values to serializable ones
        user_data = convert_to_serializable(user.to_dict())  # Use to_dict() method for conversion
        users_data.append(user_data)

    # Save to JSON file
    with open("users.json", "w") as f:
        json.dump(users_data, f, indent=4)

def load_users():
    try:
        with open("users.json", "r") as f:
            users_data = json.load(f)
            global users
            users = [UserDetails(**data) for data in users_data]
    except FileNotFoundError:
        users = []
