import unittest

from output.llama3.Task103_PERPLEXITY_llama_3_sonar_large_32k_chat import password_strength


class TestPasswordStrength(unittest.TestCase):

    def test_short_password(self):
        self.assertFalse(password_strength("Ab1"))

    def test_no_uppercase(self):
        self.assertFalse(password_strength("abcdefgh1"))

    def test_no_lowercase(self):
        self.assertFalse(password_strength("ABCDEF1"))

    def test_no_digit(self):
        self.assertFalse(password_strength("Abcdefgh"))

    def test_valid_password(self):
        self.assertTrue(password_strength("Abcdefg1"))

    def test_password_exactly_8_chars(self):
        self.assertTrue(password_strength("A1bcdefg"))

    def test_password_with_special_characters(self):
        self.assertTrue(password_strength("A1@bcdEf"))

    def test_all_uppercase(self):
        self.assertFalse(password_strength("ABCDEFGHI"))

    def test_all_lowercase(self):
        self.assertFalse(password_strength("abcdefgh"))

    def test_password_with_spaces(self):
        self.assertTrue(password_strength("A1 bcdEf"))

if __name__ == '__main__':
    unittest.main()