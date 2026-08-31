import unittest

from output.claude.Task73_CLAUDE_claude_3_5_sonnet_20240620 import is_valid_admin_password

class TestIsValidAdminPassword(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(is_valid_admin_password("Valid1Password$2024"))

    def test_too_short_password(self):
        self.assertFalse(is_valid_admin_password("Short1$"))

    def test_missing_uppercase(self):
        self.assertFalse(is_valid_admin_password("validpassword1$"))

    def test_missing_lowercase(self):
        self.assertFalse(is_valid_admin_password("VALIDPASSWORD1$"))

    def test_missing_digit(self):
        self.assertFalse(is_valid_admin_password("ValidPassword$"))

    def test_missing_special_char(self):
        self.assertFalse(is_valid_admin_password("ValidPassword1"))

    def test_contains_admin(self):
        self.assertFalse(is_valid_admin_password("Admin1234$"))

    def test_valid_password_with_special_chars(self):
        self.assertTrue(is_valid_admin_password("Valid1Password@#"))

    def test_contains_admin_case_insensitive(self):
        self.assertFalse(is_valid_admin_password("superadmin2024$"))

    def test_valid_password_with_longer_length(self):
        self.assertTrue(is_valid_admin_password("VeryLongValidPassword1$2024"))

if __name__ == "__main__":
    unittest.main()