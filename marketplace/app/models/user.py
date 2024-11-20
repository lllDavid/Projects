from datetime import datetime
from dataclasses import dataclass, field
from .roles import Role

@dataclass
class User:
    id: int
    username: str

@dataclass
class UserDetails:
    ip_address: str
    role: Role
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

    def increment_failed_login_attempts(self):
        self.failed_login_attempts += 1
        self.updated_at = datetime.now()

    def reset_failed_login_attempts(self):
        self.failed_login_attempts = 0
        self.updated_at = datetime.now()

    def increment_login_count(self):
        self.login_count += 1
        self.updated_at = datetime.now()

    def ban_user(self, reason: str):
        self.is_banned = True
        self.ban_reason = reason
        self.is_active = False
        self.updated_at = datetime.now()

    def unban_user(self):
        self.is_banned = False
        self.ban_reason = ''
        self.updated_at = datetime.now()

    def update_last_login(self):
        self.last_login = datetime.now()
        self.updated_at = datetime.now()

    def activate_user(self):
        self.is_active = True
        self.updated_at = datetime.now()

    def deactivate_user(self):
        self.is_active = False
        self.updated_at = datetime.now()

    def enable_two_factor(self):
        self.two_factor_enabled = True
        self.updated_at = datetime.now()

    def disable_two_factor(self):
        self.two_factor_enabled = False
        self.updated_at = datetime.now()
