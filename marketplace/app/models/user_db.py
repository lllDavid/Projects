import json
from .user import User
from datetime import datetime

class User_DB:
    users: list[User] = []

    def __init__(self):
        ...
       # self.load_users()

    def add_user(self, user: User):
        self.users.append(user)
        self.save_users()
        print(f"User {user.username} added to User DB")

    def save_users(self):
        users_data = []
        for user in self.users:
            user_data = user.__dict__.copy()
            for key, value in user_data.items():
                if isinstance(value, datetime):
                    user_data[key] = value.isoformat()
            users_data.append(user_data)

        with open("users.json", "w") as f:
            json.dump(users_data, f)

    def load_users(self):
        try:
            with open("users.json", "r") as f:
                users_data = json.load(f)
                self.users = [User(**data) for data in users_data]
        except FileNotFoundError:
            self.users = []
