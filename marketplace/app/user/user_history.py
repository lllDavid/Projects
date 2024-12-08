from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserHistory:
    login_count: int  
    failed_login_count: int = 0
    last_login: datetime | None = None
    last_failed_login: datetime | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def increment_login_count(self):
        self.login_count += 1
        print(f"Current login count: {self.login_count}")

    def increment_failed_login_count(self):
        self.failed_login_count += 1
        print(f"Current failed login count: {self.failed_login_count}")

    def reset_failed_login_count(self):
        self.failed_login_count = 0
        print("Failed login count reset.")

    def update_last_failed_login(self):
        self.last_failed_login = datetime.now()
        print(f"Last failed login updated to {self.last_failed_login}")

    def update_last_login(self):
        self.last_login = datetime.now()
        print(f"Last login updated to {self.last_login}")

    def display_login_history(self):
        return (f"Login count: {self.login_count}, "
                f"Last login: {self.last_login}"
                f"Failed login count: {self.failed_login_count}, "
                f"Last failed login: {self.last_failed_login}, ")

    def __str__(self):
        return (f"Login count: {self.login_count}, "
                f"Last login: {self.last_login}"
                f"Failed login count: {self.failed_login_count}, "
                f"Last failed login: {self.last_failed_login}, ")