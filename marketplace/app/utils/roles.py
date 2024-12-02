from enum import Enum, auto

class Role(Enum):
    USER = 1
    SUPPORT = 2
    ADMIN = 3

def check_permission(role: Role, required_role: Role):
    if role == required_role or role == Role.ADMIN:
        return True
    return False
