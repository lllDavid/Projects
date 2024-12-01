from dataclasses import dataclass
from datetime import datetime
from typing import List

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
