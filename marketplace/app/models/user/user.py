from dataclasses import dataclass

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

    def display_details(self):
        return (f"Username: {self.username}\n"
                f"Email: {self.email}\n")

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"



