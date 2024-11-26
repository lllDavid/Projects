from enum import Enum, auto

class Role(Enum):
    USER = auto()
    SUPPORT = auto()
    ADMIN = auto()

class RolePermissions:
    permissions = {
        Role.ADMIN: {
            'create_coin': True,
            'edit_coin': True,
            'delete_coin': True,
            'create_user': True,
            'edit_user': True,
            'delete_user': True,
        },
        Role.SUPPORT: {
            'create_coin': False,
            'edit_coin': False,
            'delete_coin': False,
            'create_user': False,
            'edit_user': True,
            'delete_user': False,
        },
        Role.USER: {
            'edit_user_profile': True,
            'change_user_email': True,
            'view_coins': True,
            'delete_user': False,
            'create_user': False,
            'edit_user': False,
            'delete_coin': False,
            'create_coin': False,
            'edit_coin': False,
        },
    }

    @staticmethod
    def can(role: Role, action: str) -> bool:
        return RolePermissions.permissions.get(role, {}).get(action, False)


