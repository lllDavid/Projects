from mariadb import connect
from app.models.user.user_details import UserDetails
from app.utils.roles import Role

conn = connect(
    user="root",       
    password="root",   
    host="localhost",           
    port=3306,                  
    database="marketplace"  
)

class UserManager:
    
    def get_user_by_username(self, username: str) -> UserDetails | None:
        """Retrieve a user by their username"""
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username, email, role FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # Assuming you need to fetch user details, security, status, and history
            user_details = self.get_user_details(user[0])  # Fetch details by user_id
            return user_details
        return None
    
    def get_user_by_email(self, email: str) -> UserDetails | None:
        """Retrieve a user by their email"""
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username, email, role FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            user_details = self.get_user_details(user[0])  # Fetch details by user_id
            return user_details
        return None
    
    def update_user_security(self, user_id: int, two_factor_enabled: bool, two_factor_secret_key: str) -> bool:
        """Update the 2FA settings for a user"""
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
        """Update the user's status"""
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
        """Update the user's login history"""
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
        """Fetch all the details related to a user from different tables"""
        # Get the user details
        user = self.get_user(user_id)
        if not user:
            return None
        
        # Get the user's security, status, and history details
        security = self.get_user_security(user_id)
        status = self.get_user_status(user_id)
        history = self.get_user_history(user_id)
        
        # Create a UserDetails object with all the gathered data
        user_details = UserDetails(
            user=user, 
            security=security, 
            status=status, 
            history=history
        )
        
        return user_details

    def get_user(self, user_id: int):
        """Fetch user basic details from the database"""
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username, email, role FROM users WHERE user_id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            return {
                "user_id": user[0],
                "username": user[1],
                "email": user[2],
                "role": Role(user[3]) 
            }
        return None
    
    def get_user_security(self, user_id: int):
        """Fetch user security details from the database"""
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash, two_factor_enabled, two_factor_secret_key FROM user_security WHERE user_id = %s", (user_id,))
        security = cursor.fetchone()
        cursor.close()
        if security:
            return {
                "password_hash": security[0],
                "two_factor_enabled": security[1],
                "two_factor_secret_key": security[2]
            }
        return None

    def get_user_status(self, user_id: int):
        """Fetch user status details from the database"""
        cursor = conn.cursor()
        cursor.execute("SELECT is_banned, ban_reason, ban_duration FROM user_status WHERE user_id = %s", (user_id,))
        status = cursor.fetchone()
        cursor.close()
        if status:
            return {
                "is_banned": status[0],
                "ban_reason": status[1],
                "ban_duration": status[2]
            }
        return None

    def get_user_history(self, user_id: int):
        """Fetch user login history from the database"""
        cursor = conn.cursor()
        cursor.execute("SELECT login_count, last_successful_login, last_failed_login, failed_login_attempts, created_at, updated_at FROM user_history WHERE user_id = %s", (user_id,))
        history = cursor.fetchone()
        cursor.close()
        if history:
            return {
                "login_count": history[0],
                "last_successful_login": history[1],
                "last_failed_login": history[2],
                "failed_login_attempts": history[3],
                "created_at": history[4],
                "updated_at": history[5]
            }
        return None
