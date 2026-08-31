import unittest

from output.llama3.Task73_PERPLEXITY_llama_3_sonar_large_32k_chat import check_password
class TestCheckPassword(unittest.TestCase):

    def test_valid_password(self):
        password = "Valid1Password$2024"
        self.assertTrue(check_password(password))

    def test_invalid_password_short(self):
        password = "Short1$"
        self.assertFalse(check_password(password))

    def test_invalid_password_missing_uppercase(self):
        password = "validpassword1$"
        self.assertFalse(check_password(password))

    def test_invalid_password_missing_lowercase(self):
        password = "VALIDPASSWORD1$"
        self.assertFalse(check_password(password))

    def test_invalid_password_missing_digit(self):
        password = "ValidPassword$"
        self.assertFalse(check_password(password))

    def test_valid_password_with_special_chars(self):
        password = "Valid1Password@#"
        self.assertTrue(check_password(password))

    def test_valid_longer_password(self):
        password = "VeryLongValidPassword1$2024"
        self.assertTrue(check_password(password))

    def test_valid_password_no_special_chars(self):
        password = "ValidPassword1"
        self.assertTrue(check_password(password))

    def test_invalid_password_with_digit(self):
        password = "Admin@1234"
        self.assertTrue(check_password(password))

    def test_valid_password_with_minimal_criteria(self):
        password = "A1bcdefg"
        self.assertTrue(check_password(password))

if __name__ == "__main__":
    unittest.main()