from dataclasses import dataclass
from datetime import datetime
from typing import List
from random import randint
from argon2 import PasswordHasher

@dataclass
class UserSecurity:
    password_hash: str 
    two_factor_enabled: bool
    two_factor_backup_codes: List[str] 
    hashed_two_factor_backup_codes: List[str] 
    two_factor_code: str 
    two_factor_code_expiry: datetime

    ph = PasswordHasher()

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

    def generate_backup_codes(self, num_codes: int = 6) -> List[str]:
        """Generate a list of random backup codes."""
        return [str(randint(100000, 999999)) for _ in range(num_codes)]

    def hash_backup_codes(self, backup_codes: List[str]) -> List[str]:
        """Hash a list of backup codes using PasswordHasher."""
        return [self.ph.hash(code) for code in backup_codes]

    def display_security_info(self):
        return (f"2FA Enabled: {self.two_factor_enabled}\n"
                f"2FA Code: {self.two_factor_code}\n"
                f"Backup Codes: {self.two_factor_backup_codes}")

    def __str__(self):
        return f"2FA Enabled: {self.two_factor_enabled}, 2FA Code Expiry: {self.two_factor_code_expiry}"
