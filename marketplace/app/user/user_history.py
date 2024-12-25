from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserHistory:
    login_count: int 
    last_login: datetime | None
    failed_login_count: int 
    last_failed_login: datetime | None 
    created_at: datetime | None 
    updated_at: datetime | None 

    def increment_login_count(self):
        self.login_count += 1
        self.update_updated_at()
    
    def update_last_login(self):
        self.last_login = datetime.now()
        self.update_updated_at()

    def increment_failed_login_count(self):
        self.failed_login_count += 1
        self.update_updated_at()

    def update_last_failed_login(self):
        self.last_failed_login = datetime.now()
        self.update_updated_at()

    def reset_failed_login_count(self):
        self.failed_login_count = 0
        self.update_updated_at()

    def initialize_created_at(self):
        self.created_at = datetime.now()

    def update_updated_at(self):
        self.updated_at = datetime.now()
    
    def __str__(self):
        return (f"Login count: {self.login_count}, "
                f"Last login: {self.last_login}, "
                f"Failed login count: {self.failed_login_count}, "
                f"Last failed login: {self.last_failed_login}, "
                f"Created at: {self.created_at}, "
                f"Updated at: {self.updated_at}")
