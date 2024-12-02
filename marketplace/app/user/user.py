from dataclasses import dataclass
from marketplace.utils.roles import Role

@dataclass
class User:
    username: str
    email: str
    password: str
    role: Role
    
    def update_username(self, new_username: str):
        self.email = new_username
        print(f"Email updated to {new_username}")

    def update_email(self, new_email: str):
        self.email = new_email
        print(f"Email updated to {new_email}")

    def update_password(self, new_password: str):
        self.password = new_password
        print("Password updated.")

    def update_role(self, new_role: Role):
        self.role = new_role
        print(f"Role updated to {new_role}")

    def display_details(self):
        return (f"Username: {self.username}\n"
                f"Email: {self.email}\n"
                f"Role: {self.role}\n")

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Role: {self.role}"

    




