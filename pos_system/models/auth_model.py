from enum import Enum

class Auth(Enum):
    USER : 1
    ELEVATED_USER : 2
    SERVICE_AGENT : 3
    ADMIN : 4

    
