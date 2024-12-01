from dataclasses import dataclass
from datetime import datetime
from app.models.user.user import User
from app.utils.roles import Role
from app.models.user.user_security import UserSecurity
from app.models.user.user_status import UserStatus
from app.models.user.user_login_history import UserLoginHistory

@dataclass
class UserDetails:
    user: User
    role: Role
    security: UserSecurity
    status: UserStatus
    login_history: UserLoginHistory
    created_at: datetime 
    updated_at: datetime 
    
    def update_user(self, new_user:User):
        self.user = new_user
        self.updated_at = datetime.now()

    def update_role(self, new_role: Role):
        self.role = new_role
        self.updated_at = datetime.now()
        print(f"Role updated to {new_role}")
    
    def update_security(self, new_security: UserSecurity):
        self.security = new_security
        self.updated_at = datetime.now()
        print("Security info updated.")

    def update_status(self, new_status: UserStatus):
        self.status = new_status
        self.updated_at = datetime.now()
        print("Status updated.")

    def update_login_history(self, new_login_history: UserLoginHistory):
        self.login_history = new_login_history
        self.updated_at = datetime.now()
        print("Login history updated.")

    def display_details(self):
        return (f"User Details:\n"
                f"User: {self.user}\n"
                f"Role: {self.role}\n"
                f"Security: {self.security}\n"
                f"Status: {self.status}\n"
                f"Login History: {self.login_history}\n"
                f"Created At: {self.created_at}\n"
                f"Updated At: {self.updated_at}")

    def __str__(self):
        return (f"User: {self.user}, Role: {self.role}, Created At: {self.created_at}, Updated At: {self.updated_at}")
