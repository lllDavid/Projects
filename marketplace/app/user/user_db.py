from mariadb import connect
from marketplace.config import Config
from marketplace.app.user.user_details import UserDetails

conn = connect(
    user=Config.DB_CONFIG["user"],       
    password=Config.DB_CONFIG["password"],   
    host=Config.DB_CONFIG["host"],           
    port=Config.DB_CONFIG["port"],                  
    database=Config.DB_CONFIG["database"]  
)

def insert_user(user_details: UserDetails):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)", 
                       (user_details.user.username, user_details.user.email, user_details.user.password, user_details.user.role.value))  
        user_id = cursor.lastrowid
        
        cursor.execute("INSERT INTO user_security (user_id, password_hash, two_factor_enabled, two_factor_secret_key) VALUES (%s, %s, %s, %s)",
                       (user_id, user_details.security.password_hash, user_details.security.two_factor_enabled, user_details.security.two_factor_secret_key))
        
        cursor.execute("INSERT INTO user_status (user_id, is_banned, ban_reason, ban_duration) VALUES (%s, %s, %s, %s)", 
                       (user_id, user_details.status.is_banned, user_details.status.ban_reason, user_details.status.ban_duration))
        
        cursor.execute("INSERT INTO user_history (user_id, login_count, failed_login_count, last_login, last_failed_login, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (user_id, user_details.history.login_count, user_details.history.failed_login_count, user_details.history.last_login, user_details.history.last_failed_login, user_details.history.created_at, user_details.history.updated_at))

        conn.commit()
        print("User and associated details inserted into the database.")
        
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

def update_user(user_id: int, user_details: UserDetails):
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET username = %s, email = %s, password = %s, role = %s WHERE user_id = %s", 
                       (user_details.user.username, user_details.user.email, user_details.user.password, user_details.user.role.value, user_id))  
        
        cursor.execute("UPDATE user_security SET password_hash = %s, two_factor_enabled = %s, two_factor_secret_key = %s WHERE user_id = %s",
                       (user_details.security.password_hash, user_details.security.two_factor_enabled, user_details.security.two_factor_secret_key, user_id))
        
        cursor.execute("UPDATE user_status SET is_banned = %s, ban_reason = %s, ban_duration = %s WHERE user_id = %s", 
                       (user_details.status.is_banned, user_details.status.ban_reason, user_details.status.ban_duration, user_id))
        
        cursor.execute("UPDATE user_history SET login_count = %s, failed_login_count = %s, last_login = %s, last_failed_login = %s, updated_at = %s WHERE user_id = %s", 
                       (user_details.history.login_count, user_details.history.failed_login_count, user_details.history.last_login, user_details.history.last_failed_login, user_details.history.updated_at, user_id))

        conn.commit()
        print("User details updated successfully.")
        
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

def update_user_security(user_id: int, two_factor_enabled: bool, two_factor_secret_key: str) -> bool:
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

def update_user_status(user_id: int, is_online: bool, is_banned: bool) -> bool:
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

def update_user_history(user_id: int, login_count: int) -> bool:
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

def delete_user(user_id: int):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM user_history WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM user_status WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM user_security WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))

        conn.commit()
        print("User and associated data deleted successfully.")
        
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()
