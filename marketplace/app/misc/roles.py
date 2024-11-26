from enum import Enum, auto

class Role(Enum):
    USER = auto()
    SUPPORT = auto()
    ADMIN = auto()

    def can_create_coin(self):
        return self in {Role.ADMIN}

    def can_edit_coin(self):
        return self in {Role.ADMIN}

    def can_delete_coin(self):
        return self in {Role.ADMIN}
    
    def can_create_user(self):
        return self in {Role.ADMIN}
    
    def can_edit_user(self):
        return self in {Role.SUPPORT, Role.ADMIN}
    
    def can_delete_user(self):
        return self in {Role.ADMIN}

    def can_view(self):
        return self in {Role.USER, Role.SUPPORT, Role.ADMIN}

    def can_access_backup_codes(self):
        # Only Admins can access or edit backup codes
        return self == Role.ADMIN

    def can_edit_backup_codes(self):
        # Only Admins can edit backup codes
        return self == Role.ADMIN
