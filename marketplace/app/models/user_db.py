from dataclasses import dataclass
from user import User

@dataclass
class User_DB:
    users: list[str] = []

    def add_user(self, user:User):
        self.users.append(str(user))
        print(f"User {user.username} added to User DB")

