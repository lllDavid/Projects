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

def insert_user(user_details: UserDetails):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)", 
                   (user_details.user.username, user_details.user.email, user_details.user.password, user_details.user.role.value))  # Use role.value to insert the integer
    user_id = cursor.lastrowid
    cursor.execute("INSERT INTO user_security (user_id, password_hash, two_factor_enabled, two_factor_secret_key) VALUES (%s, %s, %s, %s)",
                   (user_id, user_details.security.password_hash, user_details.security.two_factor_enabled, user_details.security.two_factor_secret_key))
    cursor.execute("INSERT INTO user_status (user_id, is_banned, ban_reason, ban_duration) VALUES (%s, %s, %s, %s)", 
                   (user_id, user_details.status.is_banned, user_details.status.ban_reason, user_details.status.ban_duration))
    cursor.execute("INSERT INTO user_history (user_id, login_count, last_successful_login, last_failed_login, failed_login_attempts, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                   (user_id, user_details.history.login_count, user_details.history.last_successful_login, user_details.history.last_failed_login, user_details.history.failed_login_attempts, user_details.history.created_at, user_details.history.updated_at))
    conn.commit()
    cursor.close()
    print("User and associated details inserted into the database.")

def update_user(user_id: int, user_details: UserDetails):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = %s, email = %s, password = %s, role = %s WHERE user_id = %s", 
                   (user_details.user.username, user_details.user.email, user_details.user.password, user_details.user.role.value, user_id))  # Use role.value to update the integer
    cursor.execute("UPDATE user_security SET password_hash = %s, two_factor_enabled = %s, two_factor_secret_key = %s WHERE user_id = %s",
                   (user_details.security.password_hash, user_details.security.two_factor_enabled, user_details.security.two_factor_secret_key, user_id))
    cursor.execute("UPDATE user_status SET is_banned = %s, ban_reason = %s, ban_duration = %s WHERE user_id = %s", 
                   (user_details.status.is_banned, user_details.status.ban_reason, user_details.status.ban_duration, user_id))
    cursor.execute("UPDATE user_history SET login_count = %s, last_successful_login = %s, last_failed_login = %s, failed_login_attempts = %s, updated_at = %s WHERE user_id = %s", 
                   (user_details.history.login_count, user_details.history.last_successful_login, user_details.history.last_failed_login, user_details.history.failed_login_attempts, user_details.history.updated_at, user_id))
    conn.commit()
    cursor.close()
    print("User details updated successfully.")

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

def get_user(user_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, email, role FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return {
            "user_id": user[0],
            "username": user[1],
            "email": user[2],
            "role": Role(user[3])  # Convert role value to the corresponding Role enum
        }
    return None

def get_user_security(user_id: int):
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

def get_user_status(user_id: int):
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

def get_user_history(user_id: int):
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