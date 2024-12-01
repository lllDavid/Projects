from mariadb import connect
from app.models.user.user_details import UserDetails

conn = connect(
    user="root",       
    password="root",   
    host="localhost",           
    port=3306,                  
    database="marketplace"  
)

def insert_user(user_details: UserDetails):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                   (user_details.user.username, user_details.user.email, user_details.user.password))

    user_id = cursor.lastrowid
    
    cursor.execute("INSERT INTO user_security (user_id, password_hash, two_factor_enabled, two_factor_secret_key) VALUES (%s, %s, %s, %s)",
                   (user_id, user_details.security.password_hash, user_details.security.two_factor_enabled, user_details.security.two_factor_secret_key))
    
    cursor.execute("INSERT INTO user_status (user_id, is_banned, ban_reason, ban_duration) VALUES (%s, %s, %s, %s)", 
                   (user_id, user_details.status.is_banned, user_details.status.ban_reason, user_details.status.ban_duration))
    
    cursor.execute("INSERT INTO user_history (user_id, login_count, last_successful_login, last_failed_login, failed_login_attempts, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                   (user_id, user_details.history.login_count))
    
    conn.commit()
    cursor.close()
    print("User and associated details inserted into the database.")

def update_user(user_id: int, user_details: UserDetails):
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET username = %s, email = %s, password = %s WHERE user_id = %s", 
                   (user_details.user.username, user_details.user.email, user_details.user.password, user_id))

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
