from datetime import datetime
from dataclasses import dataclass
from .roles import Role

@dataclass
class User:
    id: int
    username: str
    email: str
    password: str 

@dataclass
class UserSecurity:
    two_factor_enabled: bool
    password_hash: str
    reset_email: str
    is_verified: bool

    def enable_two_factor(self):
        self.two_factor_enabled = True

    def disable_two_factor(self):
        self.two_factor_enabled = False

    def update_password(self, new_password_hash: str):
        self.password_hash = new_password_hash

    def verify_account(self):
        self.is_verified = True

    def reset_password(self):
        print("Password reset process initiated")

@dataclass
class UserStatus:
    is_banned: bool
    ban_reason: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    def ban(self, reason: str):
        self.is_banned = True
        self.ban_reason = reason
        self.updated_at = datetime.now()

    def unban(self):
        self.is_banned = False
        self.ban_reason = ""
        self.updated_at = datetime.now()

    def set_active(self, active: bool):
        self.is_active = active
        self.updated_at = datetime.now()

    def get_account_age(self) -> str:
        delta = datetime.now() - self.created_at
        return f"{delta.days} days"

    def get_status(self) -> str:
        status = "Active" if self.is_active else "Inactive"
        status += ", Banned" if self.is_banned else ""
        return status

@dataclass
class UserLoginHistory:
    login_count: int
    failed_login_attempts: int
    last_login: datetime

    def record_login(self):
        self.login_count += 1
        self.last_login = datetime.now()

    def record_failed_login(self):
        self.failed_login_attempts += 1

    def get_last_login(self) -> str:
        return self.last_login.strftime('%Y-%m-%d %H:%M:%S') if self.last_login else "No logins yet"

@dataclass
class UserDetails:
    ip_address: str
    role: Role  
    reset_email: str
    password_hash: str
    security: UserSecurity
    status: UserStatus
    login_history: UserLoginHistory
    user: User  

    def set_reset_email(self, reset_email:str):
        self.reset_email = reset_email

    def update_ip_address(self, new_ip: str):
        self.ip_address = new_ip

    def update_password(self, new_password_hash: str):
        self.password_hash = new_password_hash
        self.security.update_password(new_password_hash)

    def get_role(self) -> str:
        return str(self.role)

    def set_status(self, is_active: bool, is_banned: bool, ban_reason:str):
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
            "security_verified": self.security.is_verified
        }

    def reset_password(self):
        self.security.reset_password()
        print(f"Password reset for {self.user.username} initiated")

    def record_login(self):
        self.login_history.record_login()

    def record_failed_login(self):
        self.login_history.record_failed_login()
