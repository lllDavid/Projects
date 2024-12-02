from dataclasses import dataclass
from app.models.user.user import User
from app.utils.roles import Role
from app.models.user.user_security import UserSecurity
from app.models.user.user_status import UserStatus
from app.models.user.user_history import UserHistory

@dataclass
class UserDetails:
    user: User
    security: UserSecurity
    status: UserStatus
    history: UserHistory

    def update_user(self, new_user: User):
        self.user = new_user
        print(f"User updated to {new_user}")

    def update_security(self, new_security: UserSecurity):
        self.security = new_security
        print("Security info updated.")

    def update_status(self, new_status: UserStatus):
        self.status = new_status
        print("Status updated.")

    def update_history(self, new_history: UserHistory):
        self.history = new_history
        print("Login history updated.")

    def display_details(self):
        return (f"User Details:\n"
                f"User: {self.user}\n"
                f"Security: {self.security}\n"
                f"Status: {self.status}\n"
                f"Login History: {self.history}\n")

    def __str__(self):
        return (f"User: {self.user}, Security: {self.security}, "
                f"Status: {self.status}, Login History: {self.history}")

