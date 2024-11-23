from datetime import datetime, timedelta
from dataclasses import dataclass
from .roles import Role
import random
import string
import hashlib


@dataclass
class User:
    id: int
    username: str
    email: str
    password:str

@dataclass
class UserSecurity:
    password_hash: str
    two_factor_enabled: bool
    two_factor_backup_codes: list[str]
    two_factor_code: str
    two_factor_code_expiry: datetime

    def enable_two_factor(self):
        self.two_factor_enabled = True
        self.generate_two_factor_code()

    def disable_two_factor(self):
        self.two_factor_enabled = False
        self.two_factor_code = ""

    def hash_password(self, password:str):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('utf-8'))
        return sha256_hash.hexdigest()

    def update_password(self, new_password_hash: str):
        self.password_hash = new_password_hash

    def reset_password(self):
        print("Password reset process initiated")

    def generate_two_factor_code(self):
        self.two_factor_code = ''.join(random.choices(string.digits, k=6))
        self.two_factor_code_expiry = datetime.now() + timedelta(minutes=5)

    def verify_two_factor_code(self, code: str) -> bool:
        if self.two_factor_code == code and datetime.now() < self.two_factor_code_expiry:
            return True
        return False

    def generate_backup_codes(self) -> list[str]:
        self.two_factor_backup_codes = [
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) for _ in range(6)
        ]
        return self.two_factor_backup_codes

    def verify_backup_code(self, code: str) -> bool:
        if code in self.two_factor_backup_codes:
            self.two_factor_backup_codes.remove(code)
            return True
        return False


@dataclass
class UserStatus:
    is_online: bool
    is_banned: bool
    ban_reason: str
    ban_duration: int
    created_at: datetime
    updated_at: datetime

    def ban(self, reason: str, duration: int = 0):
        self.is_banned = True
        self.ban_reason = reason
        self.ban_duration = duration
        self.updated_at = datetime.now()

    def unban(self):
        self.is_banned = False
        self.ban_reason = ""
        self.ban_duration = 0
        self.updated_at = datetime.now()

    def set_active(self, active: bool):
        self.is_active = active
        self.updated_at = datetime.now()

    def get_account_age(self) -> str:
        delta = datetime.now() - self.created_at
        return f"{delta.days} days"

    def get_status(self) -> str:
        status = "Active" if self.is_active else "Inactive"
        if self.is_banned:
            status += f", Banned: {self.ban_reason}"
        return status

@dataclass
class UserLoginHistory:
    login_count: int
    failed_login_attempts: int
    last_failed_login: datetime = None
    last_successful_login: datetime = None

    def record_login(self):
        self.login_count += 1
        self.last_successful_login = datetime.now()

    def record_failed_login(self):
        self.failed_login_attempts += 1
        self.last_failed_login = datetime.now()

    def get_last_login(self) -> str:
        return self.last_successful_login.strftime('%Y-%m-%d %H:%M:%S') if self.last_successful_login else "No logins yet"

@dataclass
class UserDetails:
    user: User
    role: Role
    security: UserSecurity
    status: UserStatus
    login_history: UserLoginHistory
    created_at: datetime
    updated_at: datetime

    def set_reset_email(self, reset_email: str):
        self.reset_email = reset_email

    def update_ip_address(self, new_ip: str):
        self.ip_address = new_ip

    def update_password(self, new_password_hash: str):
        self.security.update_password(new_password_hash)

    def get_role(self) -> str:
        return str(self.role)

    def set_status(self, is_active: bool, is_banned: bool, ban_reason: str):
        self.status.set_active(is_active)
        if is_banned:
            self.status.ban(ban_reason)
        else:
            self.status.unban()

    def get_account_info(self) -> dict:
        return {
            "username": self.user.username,
            "email": self.user.email,
            "role": self.get_role(),
            "status": self.status.get_status(),
            "last_login": self.login_history.get_last_login(),
            "account_age": self.status.get_account_age(),
            "two_factor_enabled": self.security.two_factor_enabled,
            "failed_login_attempts": self.login_history.failed_login_attempts,
            "account_creation_date": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "last_updated_date": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }

    def reset_password(self):
        self.security.reset_password()
        print(f"Password reset for {self.user.username} initiated")

    def record_login(self):
        self.login_history.record_login()

    def record_failed_login(self):
        self.login_history.record_failed_login()
