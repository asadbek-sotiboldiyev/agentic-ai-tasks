import unittest
from src.db import DB

class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = DB()

    def test_register_and_login(self):
        username = "testuser"
        password = "testpassword"
        
        # Test registration
        self.db.register(username=username, password=password)
        user_id = self.db.login(username=username, password=password)
        self.assertIsNotNone(user_id)

    def test_login_with_wrong_password(self):
        username = "testuser"
        wrong_password = "wrongpassword"
        
        # Test login with wrong password
        self.db.register(username=username, password="testpassword")
        user_id = self.db.login(username=username, password=wrong_password)
        self.assertIsNone(user_id)

    def test_register_existing_user(self):
        username = "testuser"
        password = "testpassword"
        
        # Register the user
        self.db.register(username=username, password=password)
        
        # Attempt to register the same user again
        with self.assertRaises(Exception):
            self.db.register(username=username, password=password)

if __name__ == '__main__':
    unittest.main()