import mariadb
from ..models.user import UserDetails
# Connect to MariaDB
conn = mariadb.connect(
    user="root",       # Your MariaDB username
    password="root",   # Your MariaDB password
    host="localhost",           # Database server address (localhost if on the same machine)
    port=3306,                  # Port for MariaDB (default is 3306)
    database="marketplace"  # The database you've created
)

def insert_user(user_details: UserDetails):
    # Example of inserting data into multiple tables
    cursor = conn.cursor()

    # Insert into users table
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                   (user_details.user.username, user_details.user.email, user_details.user.password))
    
    # Assuming you have a way to get the user ID after insertion
    user_id = cursor.lastrowid
    
    # Insert into user_security table
    cursor.execute("INSERT INTO user_security (user_id, password_hash, two_factor_enabled) VALUES (%s, %s, %s)",
                   (user_id, user_details.security.password_hash, user_details.security.two_factor_enabled))
    
    # Insert into user_status table
    cursor.execute("INSERT INTO user_status (user_id, is_online, is_banned) VALUES (%s, %s, %s)", 
                   (user_id, user_details.status.is_online, user_details.status.is_banned))
    
    # Insert into user_login_history table
    cursor.execute("INSERT INTO user_login_history (user_id, login_count) VALUES (%s, %s)", 
                   (user_id, user_details.login_history.login_count))
    
    conn.commit()
    cursor.close()
    print("User and associated details inserted into the database.")
