from datetime import datetime
from .user import User
from json import dump
from json import load

users = []

def get_all_users():
    print(f"All users: {users}")

def add_user(user: User):
    users.append(user)
    save_users()
    print(f"User {user.username} added to User DB")

def delete_user(user: User):
    users.remove(user)
    print(f"User: {user} deleted from DB.")

def save_users():
    users_data = []
    for user in users:
        user_data = user.__dict__.copy()
        for key, value in user_data.items():
            if isinstance(value, datetime):
                user_data[key] = value.isoformat()
        users_data.append(user_data)

    with open("users.json", "w") as f:
        dump(users_data, f)

def load_users():
    try:
        with open("users.json", "r") as f:
            users_data = load(f)
            global users
            users = [User(**data) for data in users_data]
    except FileNotFoundError:
        users = []
