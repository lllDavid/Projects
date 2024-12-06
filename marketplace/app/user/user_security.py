from dataclasses import dataclass
from typing import List
from random import randint
from argon2 import PasswordHasher
import pyotp

@dataclass
class UserSecurity:
    password_hash: str
    two_factor_enabled: bool
    two_factor_secret_key: str
    two_factor_backup_codes: List[str]
    two_factor_backup_codes_hash: List[str]

    @staticmethod
    def hash_password(password: str, time_cost: int = 2, memory_cost: int = 102400, parallelism: int = 8):
        ph = PasswordHasher(time_cost=time_cost, memory_cost=memory_cost, parallelism=parallelism)
        hashed_password = ph.hash(password)
        return hashed_password
    
    @staticmethod
    def validate_password_hash(attempt_hash: str, db_hash: str) -> bool:
        return attempt_hash == db_hash

    def verify_2fa_code(self, user_provided_code: str) -> bool:
        if not self.two_factor_enabled:
            return False  
        
        totp = pyotp.TOTP(self.secret_key)
        
        return totp.verify(user_provided_code)

    def generate_secret_key(self):
        totp = pyotp.TOTP(pyotp.random_base32())
        self.secret_key = totp.secret

    def display_qr_code(self, username: str):
        totp = pyotp.TOTP(self.secret_key)
        uri = totp.provisioning_uri(username, issuer_name="MyApp")
        print(f"Scan this QR code in your 2FA app: {uri}")

    def generate_backup_codes(self, num_codes: int = 6) -> List[str]:
        return [str(randint(100000, 999999)) for _ in range(num_codes)]

    def hash_backup_codes(self, backup_codes: List[str]) -> List[str]:
        ph = PasswordHasher()
        return [ph.hash(code) for code in backup_codes]

    def display_security_info(self):
        return (f"Password Hash: {self.password_hash}\n"
                f"2FA Enabled: {self.two_factor_enabled}\n"
                f"Hashed Backup Codes: {self.two_factor_backup_codes_hash}")

    def __str__(self):
        return (f"Password Hash: {self.password_hash}, "
                f"2FA Enabled: {self.two_factor_enabled}, "
                f"Hashed Backup Codes: {self.two_factor_backup_codes_hash}")
