from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from app.security.roles import Role

@dataclass
class User:
    username: str
    email: str
    password: str

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"


@dataclass
class UserSecurity:
    password_hash: str 
    two_factor_enabled: bool
    two_factor_backup_codes: List[str] 
    hashed_two_factor_backup_codes: List[str] 
    two_factor_code: str 
    two_factor_code_expiry: Optional[datetime]

    def __str__(self):
        return (f"2FA Enabled: {self.two_factor_enabled}")

@dataclass
class UserStatus:
    is_online: bool 
    is_banned: bool 
    ban_reason: str 
    ban_duration: int    
    created_at: datetime 
    updated_at: datetime 

    def __str__(self):
        return (f"Online: {self.is_online}, "
                f"Banned: {self.is_banned}, "
                f"Ban Reason: {self.ban_reason}, "
                f"Ban Duration: {self.ban_duration}, "
                f"Created At: {self.created_at}, "
                f"Updated At: {self.updated_at})")


@dataclass
class UserLoginHistory:
    login_count: int 
    failed_login_attempts: int 
    last_failed_login: Optional[datetime] 
    last_successful_login: Optional[datetime]

    def __str__(self):
        return (f"Login Count: {self.login_count}, "
                f"Failed Attempts: {self.failed_login_attempts}, "
                f"Last Failed: {self.last_failed_login}, "
                f"Last Successful: {self.last_successful_login}")


@dataclass
class UserDetails:
    user: User
    role: Role 
    security: UserSecurity
    status: UserStatus
    login_history: UserLoginHistory
    created_at: datetime 
    updated_at: datetime 

    def __str__(self):
        return (f"User Details:\n"
                f"{self.user}\n"
                f"Role: {self.role}\n"
                f"{self.security}\n"
                f"{self.status}\n"
                f"{self.login_history}\n"
                f"Created At: {self.created_at}\n"
                f"Updated At: {self.updated_at}")
