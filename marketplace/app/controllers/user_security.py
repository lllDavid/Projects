import random
import string
from datetime import datetime, timedelta
from typing import Optional
from ..models.user import UserSecurity 

class UserSecurityService:
    def __init__(self):
        self.two_factor_enabled = False
        self.reset_email = ""
        self.two_factor_code = None
        self.two_factor_code_expiry = None
    
    def create_security(self, email: str, password: str) -> UserSecurity:
        """Creates a UserSecurity object, possibly with 2FA disabled initially."""
        return UserSecurity(
            two_factor_enabled=False,
            password_hash="",
            reset_email="",
            two_factor_code=None,
            two_factor_code_expiry=None,
            is_verified=False
        )

    def enable_two_factor(self, user: UserSecurity) -> bool:
        """Enable 2FA for the user by generating a 2FA code."""
        if user.two_factor_enabled:
            return False  # Already enabled

        user.two_factor_enabled = True
        user.two_factor_code = self._generate_2fa_code()
        user.two_factor_code_expiry = datetime.now() + timedelta(minutes=10)  # Valid for 10 minutes
        return True

    def disable_two_factor(self, user: UserSecurity) -> bool:
        """Disable 2FA for the user."""
        if not user.two_factor_enabled:
            return False  # Already disabled

        user.two_factor_enabled = False
        user.two_factor_code = None
        user.two_factor_code_expiry = None
        return True

    def verify_two_factor_code(self, user: UserSecurity, code: str) -> bool:
        """Verify the 2FA code provided by the user."""
        if user.two_factor_code_expiry and datetime.now() > user.two_factor_code_expiry:
            return False  # Code expired

        return user.two_factor_code == code

    def initiate_password_reset(self, user: UserSecurity, reset_email: str) -> bool:
        """Initiates the password reset process by setting the reset email and expiry."""
        user.reset_email = reset_email
        # Send reset email logic goes here (e.g., via email service)
        return True

    def verify_reset_email(self, user: UserSecurity, reset_email: str) -> bool:
        """Verifies if the reset email matches and is not expired."""
        return user.reset_email == reset_email

    def _generate_2fa_code(self) -> str:
        """Generates a random 6-digit code for 2FA."""
        return ''.join(random.choices(string.digits, k=6))
