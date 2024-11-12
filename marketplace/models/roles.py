from enum import Enum, auto

class Roles(Enum):
    USER: auto()
    ELEVATED_USER: auto()
    SERVICE: auto()
    ADMIN: auto()

