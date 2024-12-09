from mariadb import connect
from marketplace.config import Config
from marketplace.utils.roles import Role
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
        cursor.execute("INSERT INTO users (username, email, role) VALUES (%s, %s, %s)", 
                       (user_details.user.username, user_details.user.email, user_details.user.role.value))  
        user_id = cursor.lastrowid 
        
        cursor.execute("INSERT INTO user_security (user_id, password_hash, two_factor_enabled, two_factor_backup_codes_hash, two_factor_secret_key) VALUES (%s, %s, %s, %s, %s)",
                       (user_id, user_details.user_security.password_hash, user_details.user_security.two_factor_enabled, user_details.user_security.two_factor_backup_codes_hash, user_details.user_security.two_factor_secret_key))
        
        cursor.execute("INSERT INTO user_status (user_id, is_banned, ban_reason, ban_duration) VALUES (%s, %s, %s, %s)", 
                       (user_id, user_details.user_status.is_banned, user_details.user_status.ban_reason, user_details.user_status.ban_duration))
        
        cursor.execute("INSERT INTO user_history (user_id, login_count, failed_login_count, last_login, last_failed_login, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (user_id, user_details.user_history.login_count, user_details.user_history.failed_login_count, user_details.user_history.last_login, user_details.user_history.last_failed_login, user_details.user_history.created_at, user_details.user_history.updated_at))

        conn.commit()
        print("User and associated details inserted into the database.")
        user_details.user.id = user_id
        return user_details
        
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

def update_user(user_id: int, username:str):
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET username = %s WHERE user_id = %s", 
                       (username, user_id))  
        conn.commit()
        print("User updated successfully.")
        
    except conn.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

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
