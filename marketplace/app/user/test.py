from json import dumps
from mariadb import connect

from marketplace.config import Config
from marketplace.app.user.user import User
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_profile import UserProfile
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user_fingerprint import UserFingerprint

conn = connect(
    user=Config.DB_CONFIG["user"],       
    password=Config.DB_CONFIG["password"],   
    host=Config.DB_CONFIG["host"],           
    port=Config.DB_CONFIG["port"],                  
    database=Config.DB_CONFIG["database"]  
)

def delete_user(user_id: int):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM user_profile WHERE id = %s", (user_id,))
        conn.commit()  
        print("User deleted from database.")
    except conn.Error as e:
        conn.rollback()  
        print(f"Error occurred: {e}")
    finally:
        cursor.close()  

delete_user(1)