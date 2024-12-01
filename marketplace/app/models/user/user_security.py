from dataclasses import dataclass
from datetime import datetime
from typing import List
import pyotp
import qrcode

@dataclass
class UserSecurity:
    password_hash: str
    two_factor_enabled: bool
    two_factor_backup_codes: List[str]
    hashed_two_factor_backup_codes: List[str]
    two_factor_code: str
    two_factor_code_expiry: datetime

    def enable_two_factor(self):
        totp = pyotp.TOTP(pyotp.random_base32())  
        secret_key = totp.secret

        uri = totp.provisioning_uri("user@example.com", issuer_name="ExampleApp")

        qr = qrcode.make(uri)

        qr.save("qr_code.png")
        
        self.two_factor_enabled = True
        print("Two-factor authentication enabled.")
        print(f"Your secret key is: {secret_key}")
        print("A QR code has been generated and saved as 'qr_code.png'.")

    def disable_two_factor(self):
        self.two_factor_enabled = False
        print("Two-factor authentication disabled.")

    def update_two_factor_code(self, new_code: str, expiry_time: datetime):
        self.two_factor_code = new_code
        self.two_factor_code_expiry = expiry_time
        print("Two-factor code updated.")

    def generate_backup_code(self) -> str:
        # Simple backup code generation (you can implement a more secure approach)
        return f"BACKUP-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def hash_backup_code(self, code: str) -> str:
        # Simple hashing for the backup code (replace with more secure hash in production)
        import hashlib
        return hashlib.sha256(code.encode()).hexdigest()

    def display_security_info(self):
        return (f"2FA Enabled: {self.two_factor_enabled}\n"
                f"2FA Code: {self.two_factor_code}\n"
                f"Backup Codes: {self.two_factor_backup_codes}")

    def __str__(self):
        return f"2FA Enabled: {self.two_factor_enabled}, 2FA Code Expiry: {self.two_factor_code_expiry}"
