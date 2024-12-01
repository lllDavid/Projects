from dataclasses import dataclass
from argon2 import PasswordHasher

@dataclass
class User:
    username: str
    email: str
    password: str

    def update_username(self, new_username: str):
        self.email = new_username
        print(f"Email updated to {new_username}")

    def update_email(self, new_email: str):
        self.email = new_email
        print(f"Email updated to {new_email}")

    def update_password(self, new_password: str):
        self.password = new_password
        print("Password updated.")

    @staticmethod
    def hash_password(password: str, time_cost: int = 2, memory_cost: int = 102400, parallelism: int = 8):
        ph = PasswordHasher(time_cost=time_cost, memory_cost=memory_cost, parallelism=parallelism)
        
        hashed_password = ph.hash(password)
        return hashed_password

    def display_details(self):
        return (f"Username: {self.username}\n"
                f"Email: {self.email}\n")

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"



