from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from app.security.roles import Role


@dataclass
class User:
    username: str
    email: str
    password: str

    def update_email(self, new_email: str):
        self.email = new_email
        print(f"Email updated to {new_email}")

    def update_password(self, new_password: str):
        self.password = new_password
        print("Password updated.")
# TODO Password hash module here
    def display_details(self):
        return (f"Username: {self.username}\n"
                f"Email: {self.email}\n")

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"

@dataclass
class UserSecurity:
    password_hash: str 
    two_factor_enabled: bool
    two_factor_backup_codes: List[str] 
    hashed_two_factor_backup_codes: List[str] 
    two_factor_code: str 
    two_factor_code_expiry: datetime

    def enable_two_factor(self):
        self.two_factor_enabled = True
        print("Two-factor authentication enabled.")

    def disable_two_factor(self):
        self.two_factor_enabled = False
        print("Two-factor authentication disabled.")

    def update_two_factor_code(self, new_code: str, expiry_time: datetime):
        self.two_factor_code = new_code
        self.two_factor_code_expiry = expiry_time
        print("Two-factor code updated.")

    def update_backup_codes(self, new_backup_codes: List[str]):
        self.two_factor_backup_codes = new_backup_codes
        self.hashed_two_factor_backup_codes = [self.hash_code(code) for code in new_backup_codes]
        print("Two-factor backup codes updated.")
# TODO Backupcodes hash module here
    def hash_code(self, code: str) -> str:
        return f"hashed_{code}"

    def display_security_info(self):
        return (f"2FA Enabled: {self.two_factor_enabled}\n"
                f"2FA Code: {self.two_factor_code}\n"
                f"Backup Codes: {self.two_factor_backup_codes}")

    def __str__(self):
        return f"2FA Enabled: {self.two_factor_enabled}, 2FA Code Expiry: {self.two_factor_code_expiry}"

@dataclass
class UserStatus:
    is_online: bool 
    is_banned: bool 
    ban_reason: str 
    ban_duration: int    
    created_at: datetime 
    updated_at: datetime 

    def update_ban_status(self, is_banned: bool, reason: str, duration: int):
        self.is_banned = is_banned
        self.ban_reason = reason
        self.ban_duration = duration
        self.updated_at = datetime.now()
        print(f"Ban status updated: {is_banned}, Reason: {reason}, Duration: {duration}")

    def update_online_status(self, is_online: bool):
        self.is_online = is_online
        self.updated_at = datetime.now()
        print(f"Online status updated to {is_online}.")

    def display_status(self):
        return (f"Online: {self.is_online}, "
                f"Banned: {self.is_banned}, "
                f"Ban Reason: {self.ban_reason}, "
                f"Ban Duration: {self.ban_duration}, "
                f"Created At: {self.created_at}, "
                f"Updated At: {self.updated_at}")

    def __str__(self):
        return (f"Online: {self.is_online}, "
                f"Banned: {self.is_banned}, "
                f"Ban Reason: {self.ban_reason}, "
                f"Ban Duration: {self.ban_duration}, "
                f"Created At: {self.created_at}, "
                f"Updated At: {self.updated_at}")

@dataclass
class UserLoginHistory:
    login_count: int 
    failed_login_attempts: int 
    last_failed_login: datetime
    last_successful_login: datetime

    def increment_login_count(self):
        self.login_count += 1
        print(f"Login count incremented. Current count: {self.login_count}")

    def increment_failed_attempts(self):
        self.failed_login_attempts += 1
        print(f"Failed login attempts incremented. Current count: {self.failed_login_attempts}")

    def reset_failed_attempts(self):
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

@dataclass
class UserDetails:
    user: User
    role: Role
    security: UserSecurity
    status: UserStatus
    login_history: UserLoginHistory
    created_at: datetime 
    updated_at: datetime 
    '''
    def update_role(self, new_role: str):
        self.role = new_role
        self.updated_at = datetime.now()
        print(f"Role updated to {new_role}")
    '''
    def update_security(self, new_security: UserSecurity):
        self.security = new_security
        self.updated_at = datetime.now()
        print("Security info updated.")

    def update_status(self, new_status: UserStatus):
        self.status = new_status
        self.updated_at = datetime.now()
        print("Status updated.")

    def update_login_history(self, new_login_history: UserLoginHistory):
        self.login_history = new_login_history
        self.updated_at = datetime.now()
        print("Login history updated.")

    def display_details(self):
        return (f"User Details:\n"
                f"User: {self.user}\n"
                f"Role: {self.role}\n"
                f"Security: {self.security}\n"
                f"Status: {self.status}\n"
                f"Login History: {self.login_history}\n"
                f"Created At: {self.created_at}\n"
                f"Updated At: {self.updated_at}")

    def __str__(self):
        return (f"User: {self.user}, Role: {self.role}, Created At: {self.created_at}, Updated At: {self.updated_at}")
