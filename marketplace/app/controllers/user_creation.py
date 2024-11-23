from datetime import datetime
from ..models.roles import Role
from ..models.user import User, UserDetails, UserSecurity, UserStatus, UserLoginHistory
from .user_validation import validate_user_data

class UserCreator:
    def create_user(self, username: str, email: str, password: str) -> User:
        return User(id=1, username=username, email=email, password=password) 
    
    def initialize_user_security(self) -> UserSecurity:
        return UserSecurity(
            password_hash = "",
            two_factor_enabled= False,
            two_factor_backup_codes= [],
            two_factor_code="",
            two_factor_code_expiry=None
        )
  

    def initialize_user_status(self) -> UserStatus:
        return UserStatus(
            is_online=True,
            is_banned=False,
            ban_reason="",
            ban_duration=0,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

    def initialize_user_history(self) -> UserLoginHistory:
        return UserLoginHistory(
            login_count=0,
            failed_login_attempts=0,
            last_failed_login=None,
            last_successful_login=None
        )

    def initialize_user_details(self, username: str, email: str, password: str) -> UserDetails:
        user = self.create_user(username, email, password)
        security = self.initialize_user_security()
        status = self.initialize_user_status()
        login_history = self.initialize_user_history()

        return UserDetails(
            user=user,
            role=Role.USER,
            security=security,
            status=status,
            login_history=login_history,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

    def create_and_save_user(self, username: str, email: str, password: str) -> UserDetails | None:
        try:
            validate_user_data(username, email, password)

            user_details = self.initialize_user_details(username, email, password)

            print(f"Created user: {username}")
            return user_details

        except ValueError as e:
            print(f"Error: {e}")
            return None


def main():
    user_creator = UserCreator()
    username = input("Enter a username: ")
    email = input("Enter a email address: ")
    password = input("Enter a password: ")
    print(password)
    user_details = user_creator.create_and_save_user(username, email, password)
    print(user_details)

if __name__ == "__main__":
    main()