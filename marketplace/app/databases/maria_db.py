import mariadb
from datetime import datetime

# Connect to MariaDB
conn = mariadb.connect(
    user="root",       # Your MariaDB username
    password="root",   # Your MariaDB password
    host="localhost",           # Database server address (localhost if on the same machine)
    port=3306,                  # Port for MariaDB (default is 3306)
    database="marketplace"  # The database you've created
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Example: Inserting a new user into the 'users' table
def insert_user(username, email, password):
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, password))
    conn.commit()  # Commit changes to the database
    print("User inserted successfully")

# Example: Inserting a new role into the 'roles' table
def insert_role(role_name):
    query = "INSERT INTO roles (name) VALUES (%s)"
    cursor.execute(query, (role_name,))
    conn.commit()
    print("Role inserted successfully")

# Example: Assigning a role to a user (user_id and role_id are integers)
def assign_role_to_user(user_id, role_id):
    query = "INSERT INTO user_roles (user_id, role_id) VALUES (%s, %s)"
    cursor.execute(query, (user_id, role_id))
    conn.commit()
    print("Role assigned to user successfully")

# Example: Inserting user security details
def insert_user_security(user_id, password_hash, two_factor_enabled=False, two_factor_backup_codes=None):
    query = """
    INSERT INTO user_security (user_id, password_hash, two_factor_enabled, two_factor_backup_codes)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, password_hash, two_factor_enabled, two_factor_backup_codes))
    conn.commit()
    print("User security details inserted successfully")

# Example: Updating user status (e.g., ban status)
def update_user_status(user_id, is_online, is_banned, ban_reason="", ban_duration=0):
    query = """
    UPDATE user_status 
    SET is_online = %s, is_banned = %s, ban_reason = %s, ban_duration = %s, updated_at = NOW() 
    WHERE user_id = %s
    """
    cursor.execute(query, (is_online, is_banned, ban_reason, ban_duration, user_id))
    conn.commit()
    print("User status updated successfully")

# Example: Retrieving user login history
def get_user_login_history(user_id):
    query = "SELECT * FROM user_login_history WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    print(f"User login history: {result}")

# Example: Insert a new user
insert_user("john_doe", "john.doe@example.com", "hashed_password")

# Example: Insert a new role
insert_role("Admin")

# Example: Assign the 'Admin' role to a user (user_id = 1, role_id = 1)
assign_role_to_user(1, 1)

# Example: Insert security details for a user (user_id = 1)
insert_user_security(1, "hashed_password", two_factor_enabled=True, two_factor_backup_codes="code1,code2,code3")

# Example: Update a user's status (user_id = 1)
update_user_status(1, is_online=True, is_banned=False)

# Example: Get user login history (user_id = 1)
get_user_login_history(1)

# Close the cursor and connection after operations are complete
cursor.close()
conn.close()
