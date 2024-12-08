from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserHistory:
    login_count: int  
    last_successful_login: datetime | None = None
    last_failed_login: datetime | None = None
    failed_login_attempts: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def increment_login_count(self):
        self.login_count += 1
        print(f"Login count incremented. Current count: {self.login_count}")

    def increment_failed_login_attempts(self):
        if self.failed_login_attempts is None:
            self.failed_login_attempts = 0
        self.failed_login_attempts += 1
        print(f"Failed login attempts incremented. Current count: {self.failed_login_attempts}")

    def reset_failed_login_attempts(self):
        self.failed_login_attempts = 0
        print("Failed login attempts reset.")

    def update_last_failed_login(self):
        self.last_failed_login = datetime.now()
        print(f"Last failed login updated to {self.last_failed_login}")

    def update_last_successful_login(self):
        self.last_successful_login = datetime.now()
        print(f"Last successful login updated to {self.last_successful_login}")

    def display_login_history(self):
        return (f"Login Count: {self.login_count}, "
                f"Failed Attempts: {self.failed_login_attempts}, "
                f"Last Failed: {self.last_failed_login}, "
                f"Last Successful: {self.last_successful_login}")

    def __str__(self):
        return (f"Login Count: {self.login_count}, "
                f"Failed Attempts: {self.failed_login_attempts}, "
                f"Last Failed: {self.last_failed_login}, "
                f"Last Successful: {self.last_successful_login}")