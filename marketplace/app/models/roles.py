from enum import Enum, auto

class Role(Enum):
    USER = auto()
    ELEVATED_USER = auto()
    SERVICE = auto()
    ADMIN = auto()
