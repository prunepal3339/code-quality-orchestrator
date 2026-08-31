import unittest

from output.codestral.Task73_MISTRAL_codestral_latest import is_valid_password as is_valid_password

class TestIsValidPassword(unittest.TestCase):

    def test_valid_password(self):
        password = "Valid1Password$2024"
        self.assertTrue(is_valid_password(password))

    def test_too_short_password(self):
        password = "Short1$"
        self.assertFalse(is_valid_password(password))

    def test_missing_uppercase(self):
        password = "validpassword1$"
        self.assertFalse(is_valid_password(password))

    def test_missing_lowercase(self):
        password = "VALIDPASSWORD1$"
        self.assertFalse(is_valid_password(password))

    def test_missing_digit(self):
        password = "ValidPassword$"
        self.assertFalse(is_valid_password(password))

    def test_missing_special_char(self):
        password = "ValidPassword1"
        self.assertFalse(is_valid_password(password))

    def test_contains_special_chars(self):
        password = "Valid1Password@#"
        self.assertTrue(is_valid_password(password))

    def test_valid_password_with_longer_length(self):
        password = "VeryLongValidPassword1$2024"
        self.assertTrue(is_valid_password(password))

    def test_short_password_no_special_char(self):
        password = "ShortPass1"
        self.assertFalse(is_valid_password(password))

    def test_valid_password_with_mixed_chars(self):
        password = "Mix3d#Chars"
        self.assertTrue(is_valid_password(password))

if __name__ == "__main__":
    unittest.main()