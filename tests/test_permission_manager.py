import unittest
from src.permission_manager import PermissionManager, PermissionLevel

class TestPermissionManager(unittest.TestCase):
    def test_get_role_name(self):
        manager = PermissionManager()
        self.assertEqual(manager.get_role_name(PermissionLevel.ADMIN), "Admin")
        self.assertEqual(manager.get_role_name(PermissionLevel.DEVELOPER), "Developer")
        self.assertEqual(manager.get_role_name(PermissionLevel.USER), "User")

    def test_set_permission_level(self):
        manager = PermissionManager()
        manager.set_permission_level(PermissionLevel.ADMIN)
        self.assertEqual(manager.get_current_level(), PermissionLevel.ADMIN)

if __name__ == '__main__':
    unittest.main()
