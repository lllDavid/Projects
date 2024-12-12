from dataclasses import dataclass

from marketplace.app.user.user import User
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_security import UserSecurity

@dataclass
class UserDetails:
    user: User
    user_status: UserStatus
    user_history: UserHistory
    user_security: UserSecurity

    def update_user(self, new_user: User):
        self.user = new_user
        print(f"User updated.")

    def update_user_security(self, new_user_security: UserSecurity):
        self.user_security = new_user_security
        print("Security info updated.")

    def update_user_status(self, new_user_status: UserStatus):
        self.user_status = new_user_status
        print("Status updated.")

    def update_user_history(self, new_user_history: UserHistory):
        self.user_history = new_user_history
        print("User history updated.")
    
    def __str__(self):
        return (f"User: {self.user}, Security: {self.user_security}, "
                f"Status: {self.user_status}, History: {self.user_history}")

