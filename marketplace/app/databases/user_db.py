import mariadb
from ..models.user import UserDetails

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
