from output.gtp4o.Task42_OPENAI_gpt_4o import *

import unittest
class TestUserAuth(unittest.TestCase):

    def setUp(self):
        self.auth = UserAuth()
        self.auth.add_user("user", "pass")

    def test_add_user(self):
        self.auth.add_user("newuser", "newpass")
        self.assertTrue(self.auth.authenticate("newuser", "newpass"))

    def test_authenticate_success(self):
        self.assertTrue(self.auth.authenticate("user", "pass"))

    def test_authenticate_failure(self):
        self.assertFalse(self.auth.authenticate("user", "wrongpass"))

    def test_authenticate_non_existent_user(self):
        self.assertFalse(self.auth.authenticate("nonexistent", "pass"))

    def test_authenticate_with_empty_password(self):
        self.auth.add_user("emptyuser", "")
        self.assertTrue(self.auth.authenticate("emptyuser", ""))

    def test_authenticate_with_empty_username(self):
        self.auth.add_user("", "pass")
        self.assertFalse(self.auth.authenticate("", "pass"))

    def test_add_user_with_existing_username(self):
        self.auth.add_user("user", "newpass")
        self.assertTrue(self.auth.authenticate("user", "newpass"))

if __name__ == "__main__":
    unittest.main()