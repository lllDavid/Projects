from enum import Enum, auto
from .user import User

class Role(Enum):
    USER: auto()
    ELEVATED_USER: auto()
    SERVICE: auto()
    ADMIN: auto()


def get_role(user: User) -> None:
    print(f"User: {user.username} has the role: {user.role}")

