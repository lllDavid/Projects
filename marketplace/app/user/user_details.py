from dataclasses import dataclass
from marketplace.app.user.user import User
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory

@dataclass
class UserDetails:
    user: User
    user_security: UserSecurity
    user_status: UserStatus
    user_history: UserHistory

    def update_user(self, new_user: User):
        self.user = new_user
        print(f"User updated to {new_user}")

    def update_user_security(self, new_user_security: UserSecurity):
        self.user_security = new_user_security
        print("Security info updated.")

    def update_user_status(self, new_user_status: UserStatus):
        self.user_status = new_user_status
        print("Status updated.")

    def update_user_history(self, new_user_history: UserHistory):
        self.user_history = new_user_history
        print("Login history updated.")

    def display_details(self):
        return (f"User Details:\n"
                f"User: {self.user}\n"
                f"Security: {self.user_security}\n"
                f"Status: {self.user_status}\n"
                f"Login user_History: {self.user_history}\n")

    def __str__(self):
        return (f"User: {self.user}, Security: {self.user_security}, "
                f"Status: {self.user_status}, Login user_History: {self.user_history}")

