from enum import Enum

class Auth(Enum):
    USER : 1
    ELEVATED_USER : 2
    SERVICE_AGENT : 3
    ADMIN : 4

    def get_auth_role(auth_id):
        try:
            return Auth(id)
        except ValueError:
            print(f"No valid Auth ID")

    def assign_role(user_id):
        pass

    methods = []