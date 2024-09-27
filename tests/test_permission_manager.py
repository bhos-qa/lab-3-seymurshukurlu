import unittest
from src.permission_manager import PermissionManager, PermissionLevel

class TestPermissionManager(unittest.TestCase):
    def test_get_role_name(self):
        manager = PermissionManager()
        self.assertEqual(manager.get_role_name(PermissionLevel.ADMIN), "Admin")
        self.assertEqual(manager.get_role_name(PermissionLevel.DEVELOPER), "Developer")
        self.assertEqual(manager.get_role_name(PermissionLevel.USER), "User")
        
        # Test invalid role
        with self.assertRaises(ValueError):
            manager.get_role_name("InvalidRole")

    def test_set_permission_level(self):
        manager = PermissionManager()
        
        # Set and test for ADMIN level
        manager.set_permission_level(PermissionLevel.ADMIN)
        self.assertEqual(manager.get_current_level(), PermissionLevel.ADMIN)
        
        # Set and test for DEVELOPER level
        manager.set_permission_level(PermissionLevel.DEVELOPER)
        self.assertEqual(manager.get_current_level(), PermissionLevel.DEVELOPER)
        
        # Set and test for USER level
        manager.set_permission_level(PermissionLevel.USER)
        self.assertEqual(manager.get_current_level(), PermissionLevel.USER)
        
        # Test invalid permission level
        with self.assertRaises(ValueError):
            manager.set_permission_level("InvalidLevel")

if __name__ == '__main__':
    unittest.main()
