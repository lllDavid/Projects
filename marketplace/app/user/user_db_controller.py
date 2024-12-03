from mariadb import connect
from marketplace.app.user.user import User
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_details import UserDetails
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_security import UserSecurity

conn = connect(
    user="root",       
    password="root",   
    host="localhost",           
    port=3306,                  
    database="marketplace"  
)

class UserDBController:
    def get_user_by_username(self, username: str) -> UserDetails | None:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username, email, role FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            user_details = self.get_user_details(user[0])
            return user_details
        return None
    
    def get_user_by_email(self, email: str) -> UserDetails | None:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username, email, role FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            user_details = self.get_user_details(user[0])
            return user_details
        return None
    
    def update_user_security(self, user_id: int, two_factor_enabled: bool, two_factor_secret_key: str) -> bool:
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE user_security SET two_factor_enabled = %s, two_factor_secret_key = %s WHERE user_id = %s",
                           (two_factor_enabled, two_factor_secret_key, user_id))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            conn.rollback()
            print(f"Error updating user security: {e}")
            cursor.close()
            return False
    
    def update_user_status(self, user_id: int, is_online: bool, is_banned: bool) -> bool:
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE user_status SET is_online = %s, is_banned = %s WHERE user_id = %s", 
                           (is_online, is_banned, user_id))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            conn.rollback()
            print(f"Error updating user status: {e}")
            cursor.close()
            return False
    
    def update_user_history(self, user_id: int, login_count: int) -> bool:
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE user_history SET login_count = %s WHERE user_id = %s", 
                           (login_count, user_id))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            conn.rollback()
            print(f"Error updating user history: {e}")
            cursor.close()
            return False
    
    def get_user_details(self, user_id: int) -> UserDetails | None:
        user = self.get_user(user_id)
        if not user:
            return None
        security = self.get_user_security(user_id)
        if not security:
            return None
        status = self.get_user_status(user_id)
        if not status:
            return None
        history = self.get_user_history(user_id)
        if not history:
            return None
        
        user_details = UserDetails(
            user=user, 
            security=security, 
            status=status, 
            history=history
        )
        
        return user_details

    def get_user(self, user_id: int):
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username, email, role FROM users WHERE user_id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            return User(username=user[1], email=user[2], password=None, role=user[3])
        return None
    
    def get_user_security(self, user_id: int):
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, password_hash, two_factor_enabled, two_factor_secret_key, two_factor_backup_codes_hash FROM user_security WHERE user_id = %s", (user_id,))
        security = cursor.fetchone()
        cursor.close()
        if security:
           return UserSecurity(
            password_hash=security[1],
            two_factor_enabled=security[2],
            two_factor_secret_key=security[3],
            two_factor_backup_codes=None,
            two_factor_backup_codes_hash=security[4],
        )
        return None

    def get_user_status(self, user_id: int):
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, is_banned, ban_reason, ban_duration FROM user_status WHERE user_id = %s", (user_id,))
        status = cursor.fetchone()
        cursor.close()
        if status:
            return UserStatus(
            is_online=None,
            is_banned=status[1],
            ban_reason=status[2],
            ban_duration=status[3],
        )
        return None

    def get_user_history(self, user_id: int):
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, login_count, last_successful_login, last_failed_login, failed_login_attempts, created_at, updated_at FROM user_history WHERE user_id = %s", (user_id,))
        history = cursor.fetchone()
        cursor.close()
        if history:
           return UserHistory(
            login_count=history[1],
            last_successful_login=history[2],
            last_failed_login=history[3],
            failed_login_attempts=history[4],
            created_at=history[5],
            updated_at=history[6],
        )
        return None
