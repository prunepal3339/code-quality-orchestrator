import unittest
from output.gtp4o.Task73_OPENAI_gpt_4o import check_password

class TestCheckPassword(unittest.TestCase):

    def test_valid_password(self):
        password = "admin123"
        self.assertEqual(check_password(password), "Password is valid")

    def test_invalid_password_short(self):
        password = "Short1$"
        self.assertEqual(check_password(password), "Password is invalid")

    def test_invalid_password_missing_uppercase(self):
        password = "validpassword1$"
        self.assertEqual(check_password(password), "Password is invalid")

    def test_invalid_password_missing_lowercase(self):
        password = "VALIDPASSWORD1$"
        self.assertEqual(check_password(password), "Password is invalid")

    def test_invalid_password_missing_digit(self):
        password = "ValidPassword$"
        self.assertEqual(check_password(password), "Password is invalid")

    def test_invalid_password_with_special_chars(self):
        password = "Valid1Password@#"
        self.assertEqual(check_password(password), "Password is invalid")

    def test_invalid_longer_password(self):
        password = "VeryLongValidPassword1$2024"
        self.assertEqual(check_password(password), "Password is invalid")

    def test_invalid_password_no_special_chars(self):
        password = "ValidPassword1"
        self.assertEqual(check_password(password), "Password is invalid")

    def test_invalid_password_with_digit(self):
        password = "Admin@1234"
        self.assertEqual(check_password(password), "Password is invalid")

    def test_invalid_password_with_minimal_criteria(self):
        password = "A1bcdefg"
        self.assertEqual(check_password(password), "Password is invalid")

if __name__ == "__main__":
    unittest.main()