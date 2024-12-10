from dataclasses import dataclass
from marketplace.utils.roles import Role

@dataclass
class User:
    id: int | None
    username: str
    email: str
    role: Role

    def update_username(self, new_username: str):
        self.username = new_username
        print(f"Username changed to {new_username}")

    def update_email(self, new_email: str):
        self.email = new_email
        print(f"Email changed to {new_email}")

    def update_role(self, new_role: Role):
        self.role = new_role
        print(f"Role changed to {new_role}")

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Role: {self.role}"
