from enum import Enum

class PermissionLevel(Enum):
    ADMIN = 1
    DEVELOPER = 2
    USER = 3


class PermissionManager:
    def __init__(self):
        self._current_level = PermissionLevel.USER

    def get_role_name(self, level: PermissionLevel) -> str:
        if level == PermissionLevel.ADMIN:
            return "Admin"
        elif level == PermissionLevel.DEVELOPER:
            return "Developer"
        elif level == PermissionLevel.USER:
            return "User"
        else:
            raise ValueError("Unknown Permission Level")

    def set_permission_level(self, level: PermissionLevel):
        self._current_level = level

    def get_current_level(self) -> PermissionLevel:
        return self._current_level
