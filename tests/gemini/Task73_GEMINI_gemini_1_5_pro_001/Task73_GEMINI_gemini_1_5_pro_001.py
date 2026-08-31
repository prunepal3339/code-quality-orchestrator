import unittest

from output.gemini.Task73_GEMINI_gemini_1_5_pro_001 import is_password_valid

class TestIsPasswordValid(unittest.TestCase):

    def test_valid_password(self):
        password = "Valid1Password$2024"
        self.assertTrue(is_password_valid(password))

    def test_too_short_password(self):
        password = "Short1$"
        self.assertFalse(is_password_valid(password))

    def test_missing_uppercase(self):
        password = "validpassword1$"
        self.assertFalse(is_password_valid(password))

    def test_missing_lowercase(self):
        password = "VALIDPASSWORD1$"
        self.assertFalse(is_password_valid(password))

    def test_missing_digit(self):
        password = "ValidPassword$"
        self.assertFalse(is_password_valid(password))

    def test_valid_with_special_chars(self):
        password = "Valid1Password@#"
        self.assertTrue(is_password_valid(password))

    def test_valid_longer_password(self):
        password = "VeryLongValidPassword1$2024"
        self.assertTrue(is_password_valid(password))

    def test_missing_special_chars(self):
        password = "ValidPassword1"
        self.assertTrue(is_password_valid(password))

    def test_missing_digit_and_special_char(self):
        password = "ValidPassword"
        self.assertFalse(is_password_valid(password))

    def test_valid_minimal_criteria_password(self):
        password = "A1bcdefg"
        self.assertTrue(is_password_valid(password))

if __name__ == "__main__":
    unittest.main()