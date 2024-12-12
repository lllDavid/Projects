from datetime import datetime

from marketplace.helpers.roles import Role
from marketplace.app.user import user_db
from marketplace.app.user.user_profile import UserProfile
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user import User

class UserCreator:
    def create_user_profile(self, username: str, email: str, role: Role) -> UserProfile:
        return UserProfile(id=None, username=username, email=email, role=role)

    def create_user_status(self) -> UserStatus:
        return UserStatus(
            is_online=True,
            is_banned=False,
            ban_reason=None,
            ban_duration=None,
        )

    def create_user_history(self) -> UserHistory:
        return UserHistory(
            login_count=0,
            failed_login_count=0,
            last_login=None,
            last_failed_login=None,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    
    def create_user_security(self, password: str) -> UserSecurity:
        return UserSecurity(
            password_hash=UserSecurity.hash_password(password),
            two_factor_enabled=False,
            two_factor_secret_key=None,
            two_factor_backup_codes=None,
            two_factor_backup_codes_hash=None
        )

    def create_user(self, username: str, email: str, password: str) -> User:
        user_profile = self.create_user_profile(username, email, role=Role.USER)
        user_security = self.create_user_security(password)
        user_status = self.create_user_status()
        user_history = self.create_user_history()

        return User(
            user_profile=user_profile,
            user_security=user_security,
            user_status=user_status,
            user_history=user_history,
        )

    def create_and_save_user(self, username: str, email: str, password: str) -> User | None:
        try:
            user = self.create_user(username, email, password)
            user_db.insert_user(user)
            return user
        except ValueError as e:
            print(f"Error: {e}")
            return None 
        except Exception as e:
            print(f"Error: {e}")
            return None

        
