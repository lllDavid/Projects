import mariadb
from app.models.user import UserDetails

conn = mariadb.connect(
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
    
    cursor.execute("INSERT INTO user_security (user_id, password_hash, two_factor_enabled) VALUES (%s, %s, %s)",
                   (user_id, user_details.security.password_hash, user_details.security.two_factor_enabled))
    
    cursor.execute("INSERT INTO user_status (user_id, is_banned) VALUES (%s, %s)", 
                   (user_id, user_details.status.is_banned))
    
    cursor.execute("INSERT INTO user_login_history (user_id, login_count) VALUES (%s, %s)", 
                   (user_id, user_details.login_history.login_count))
    
    conn.commit()
    cursor.close()
    print("User and associated details inserted into the database.")

def update_user(user_id: int, user_details: UserDetails):
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET username = %s, email = %s, password = %s WHERE user_id = %s", 
                   (user_details.user.username, user_details.user.email, user_details.user.password, user_id))

    cursor.execute("UPDATE user_security SET password_hash = %s, two_factor_enabled = %s WHERE user_id = %s",
                   (user_details.security.password_hash, user_details.security.two_factor_enabled, user_id))
    
    cursor.execute("UPDATE user_status SET is_banned = %s WHERE user_id = %s", 
                   (user_details.status.is_banned, user_id))
    
    cursor.execute("UPDATE user_login_history SET login_count = %s WHERE user_id = %s", 
                   (user_details.login_history.login_count, user_id))

    conn.commit()
    cursor.close()
    print("User details updated successfully.")

def delete_user(user_id: int):
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM user_login_history WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM user_status WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM user_security WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))

        conn.commit()
        print("User and associated data deleted successfully.")
    
    except mariadb.Error as e:
        conn.rollback()
        print(f"Error occurred: {e}")
    
    finally:
        cursor.close()
