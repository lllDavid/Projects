from datetime import datetime
from ..models.user import UserDetails, User, UserSecurity, UserStatus, UserLoginHistory
from ..models.roles import Role
from .user_validation import validate_user_data

class UserCreator:
    def create_user(self, username: str, email: str, password: str) -> User:
        return User(id=1, username=username, email=email, password=password) 


    def create_user_security(self):
        return UserSecurity(
            two_factor_enabled=False,
            two_factor_code="",
            two_factor_code_expiry=datetime.now(),
            password_hash="",
            reset_email="",
            is_verified=False
        )

    def create_user_status(self) -> UserStatus:
        return UserStatus(
            is_banned=False,
            ban_reason="",
            is_active=True,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

    def create_user_login_history(self) -> UserLoginHistory:
        return UserLoginHistory(
            login_count=0,
            failed_login_attempts=0,
            last_login=datetime.now()
        )

    def create_user_details(self, username: str, email: str, password: str) -> UserDetails:
        user = self.create_user(username, email, password)
        security = self.create_user_security()
        status = self.create_user_status()
        login_history = self.create_user_login_history()

        return UserDetails(
            ip_address="",
            role=Role.USER,
            reset_email=email,
            password_hash=password,  
            security=security,
            status=status,
            login_history=login_history,
            user=user
        )

    def create_and_save_user(self, username: str, email: str, password: str) -> UserDetails | None:
        try:
            validate_user_data(username, email, password)

            user_details = self.create_user_details(username, email, password)

            print(f"Created user: {username}")
            return user_details

        except ValueError as e:
            print(f"Error: {e}")
            return None
