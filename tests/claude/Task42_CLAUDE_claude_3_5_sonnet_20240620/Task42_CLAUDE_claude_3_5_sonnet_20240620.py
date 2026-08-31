from output.claude.Task42_CLAUDE_claude_3_5_sonnet_20240620 import *
# from output.codestral.Task42_MISTRAL_codestral_latest
# from output.gemini.
# from output.gtp4o.
# from output.llama3.

import unittest

class TestUserAuthentication(unittest.TestCase):

    # Test registration with a new user
    def test_register_new_user(self):
        self.assertTrue(register("bob", "securepassword"))
        self.assertIn("bob", users)

    # Test registration with an existing user
    def test_register_existing_user(self):
        register("alice", "password123")
        self.assertFalse(register("alice", "newpassword"))

    # Test successful login with correct credentials
    def test_login_successful(self):
        register("charlie", "mypassword")
        self.assertTrue(login("charlie", "mypassword"))

    # Test login failure with incorrect password
    def test_login_failure_incorrect_password(self):
        register("david", "password")
        self.assertFalse(login("david", "wrongpassword"))

    # Test login failure with non-existent user
    def test_login_failure_non_existent_user(self):
        self.assertFalse(login("nonexistent", "password"))

    # Test successful registration and login for multiple users
    def test_multiple_users(self):
        register("eve", "pass1")
        register("frank", "pass2")
        self.assertTrue(login("eve", "pass1"))
        self.assertTrue(login("frank", "pass2"))

    # Test hash consistency
    def test_hash_consistency(self):
        password = "password"
        hash1 = hash_password(password)
        hash2 = hash_password(password)
        self.assertNotEqual(hash1, hash2)  # Should be different due to different salts
        self.assertTrue(verify_password(hash1, password))

    # Test login with altered stored password
    def test_login_with_altered_stored_password(self):
        register("grace", "password")
        altered_hash = hash_password("differentpassword")
        users["grace"] = altered_hash
        self.assertFalse(login("grace", "password"))

    # Test register and login with empty password
    def test_register_login_empty_password(self):
        self.assertTrue(register("hank", ""))
        self.assertTrue(login("hank", ""))
        self.assertFalse(login("hank", "wrongpassword"))

    # Test register and login with very long password
    def test_long_password(self):
        long_password = "a" * 1000
        self.assertTrue(register("ida", long_password))
        self.assertTrue(login("ida", long_password))
        self.assertFalse(login("ida", "shortpassword"))

if __name__ == "__main__":
    unittest.main()