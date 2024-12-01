from app.databases import user_db
from app.models.user.user_details import UserDetails
from app.models.user.user import User
from app.models.user.user_security import UserSecurity
from app.models.user.user_status import UserStatus
from app.models.user.user_history import UserHistory

class UserManager:
    def get_user_by_username(self, username: str) -> UserDetails | None:
        """Retrieve a user by their username"""
        try:
            user_details = user_db.get_user_by_username(username)  # Hypothetical database query
            return user_details
        except Exception as e:
            print(f"Error fetching user by username: {e}")
            return None

    def get_user_by_email(self, email: str) -> UserDetails | None:
        """Retrieve a user by their email"""
        try:
            user_details = user_db.get_user_by_email(email)  # Hypothetical database query
            return user_details
        except Exception as e:
            print(f"Error fetching user by email: {e}")
            return None

    def update_user_security(self, user_id: int, two_factor_enabled: bool, two_factor_secret_key: str) -> bool:
        """Update the 2FA settings for a user"""
        try:
            user_security = user_db.get_user_security(user_id)  # Fetch current user security settings
            user_security.two_factor_enabled = two_factor_enabled
            user_security.two_factor_secret_key = two_factor_secret_key
            user_db.update_user_security(user_security)  # Update in database
            return True
        except Exception as e:
            print(f"Error updating user security: {e}")
            return False

    def update_user_status(self, user_id: int, is_online: bool, is_banned: bool) -> bool:
        """Update the user's status"""
        try:
            user_status = user_db.get_user_status(user_id)  # Fetch current user status
            user_status.is_online = is_online
            user_status.is_banned = is_banned
            user_db.update_user_status(user_status)  # Update in database
            return True
        except Exception as e:
            print(f"Error updating user status: {e}")
            return False

    def update_user_history(self, user_id: int, login_count: int) -> bool:
        """Update the user's login history"""
        try:
            user_history = user_db.get_user_history(user_id)  # Fetch current user history
            user_history.login_count = login_count
            user_db.update_user_history(user_history)  # Update in database
            return True
        except Exception as e:
            print(f"Error updating user history: {e}")
            return False
