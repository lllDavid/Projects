from datetime import datetime
from app.utils.roles import Role
from app.databases import user_db
from app.models.user.user import User
from app.models.user.user_security import UserSecurity
from app.models.user.user_status import UserStatus
from app.models.user.user_history import UserHistory
from app.models.user.user_details import UserDetails
from app.utils.validation import validate_user_data


class UserCreator:
    def create_user(self, username: str, email: str, password: str) -> User:
        return User(username=username, email=email, password=password) 
    
    def initialize_user_security(self,password) -> UserSecurity:
        return UserSecurity(
            password_hash = UserSecurity.hash_password(password),
            two_factor_enabled = False,
            two_factor_backup_codes = None,
            two_factor_backup_codes_hash = None,
        )
  
    def initialize_user_status(self) -> UserStatus:
        return UserStatus(
            is_online=True,
            is_banned=False,
            ban_reason="",
            ban_duration=0,
        )

    def initialize_user_history(self) -> UserHistory:
        return UserHistory(
            login_count=0,
            last_successful_login=None,
            last_failed_login=None,
            failed_login_attempts=0,
            created_at = datetime.now(),
            updated_at= datetime.now()
        )

    def initialize_user_details(self, username: str, email: str, password: str) -> UserDetails:
        user = self.create_user(username, email, password)
        security = self.initialize_user_security(password)
        status = self.initialize_user_status()
        history = self.initialize_user_history()

        return UserDetails(
            user=user,
            role=Role.USER,
            security=security,
            status=status,
            history=history,
        )

    def create_and_save_user(self, username: str, email: str, password: str) -> UserDetails | None:
        try:
            validate_user_data(username, email, password)

            user_details = self.initialize_user_details(username, email, password)
            print(f"User {username} created successfully.")
            user_db.insert_user(user_details)
            return user_details

        except ValueError as e:
            print(f"Error: {e}")
            return None


def main():
    user_creator = UserCreator()

    username = input("Enter a username: ")
    email = input("Enter a email address: ")
    password = input("Enter a password: ")

    user_creator.create_and_save_user(username, email, password)

if __name__ == "__main__":
    main()