from datetime import datetime
from ..models.user import UserDetails
from json import dump
from json import load
from app.models.roles import Role

users = []

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
        user_data = user.__dict__.copy()
        
        for key, value in user_data.items():
            if isinstance(value, datetime):
                user_data[key] = value.isoformat()
            elif isinstance(value, Role):
                user_data[key] = value.name  

        users_data.append(user_data)

    with open("users.json", "w") as f:
        dump(users_data, f, indent=4)  

def load_users():
    try:
        with open("users.json", "r") as f:
            users_data = load(f)
            global users
            users = [UserDetails(**data) for data in users_data]
    except FileNotFoundError:
        users = []
