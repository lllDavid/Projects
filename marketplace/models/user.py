from datetime import datetime
from dataclasses import dataclass, field
import re

@dataclass
class User:
    id: int
    role: str
    ip_address: str
    username: str
    email: str
    reset_email: str
    password_hash: str
    two_factor_enabled: bool = False
    is_verified: bool = False
    is_banned: bool = False
    ban_reason: str = ''
    is_active: bool = False
    login_count: int = 0
    failed_login_attempts: int = 0
    last_login: datetime = field(default_factory=datetime.now)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        if not self._is_valid_email(self.email):
            raise ValueError(f"Invalid email format: {self.email}")

    def _is_valid_email(self, email: str) -> bool:
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(email_regex, email) is not None

    def reset_password(self, new_password_hash: str):
        self.password_hash = new_password_hash
        self.failed_login_attempts = 0  
        self.updated_at = datetime.now()
        print(f"Password reset successfully for user {self.username}")

    def increment_failed_login_attempts(self):
        self.failed_login_attempts += 1
        self.updated_at = datetime.now()
        
        if self.failed_login_attempts >= 5:
            self.ban_user("Too many failed login attempts")
        
        print(f"Failed login attempts: {self.failed_login_attempts}")

    def increment_login_count(self):
        self.login_count += 1
        self.last_login = datetime.now()
        self.updated_at = datetime.now()
        print(f"Login count: {self.login_count}, Last login: {self.last_login}")

    def ban_user(self, reason: str):
        self.is_banned = True
        self.ban_reason = reason
        self.updated_at = datetime.now()
        print(f"User {self.username} has been banned. Reason: {self.ban_reason}")

    def verify_user(self):
        self.is_verified = True
        self.updated_at = datetime.now()
        print(f"User {self.username} has been verified.")

    def is_locked(self) -> bool:
        return self.is_banned or self.failed_login_attempts >= 5

    def can_login(self) -> bool:
        if self.is_locked():
            print(f"User {self.username} is locked and cannot log in.")
            return False
        return self.is_active

    def enable_two_factor(self):
        self.two_factor_enabled = True
        self.updated_at = datetime.now()
        print(f"Two-factor authentication enabled for {self.username}")

    def disable_two_factor(self):
        self.two_factor_enabled = False
        self.updated_at = datetime.now()
        print(f"Two-factor authentication disabled for {self.username}")

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email}, is_active={self.is_active}, is_verified={self.is_verified})"
