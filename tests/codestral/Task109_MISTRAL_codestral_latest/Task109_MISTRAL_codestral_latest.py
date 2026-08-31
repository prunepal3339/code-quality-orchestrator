import unittest

from output.codestral.Task109_MISTRAL_codestral_latest import validate_input


class TestValidateInput(unittest.TestCase):

    def test_valid_input_with_letters_and_numbers(self):
        self.assertTrue(validate_input("abc123"))

    def test_valid_input_with_underscore(self):
        self.assertTrue(validate_input("user_name"))

    def test_invalid_input_with_special_characters(self):
        self.assertFalse(validate_input("user@name"))

    def test_invalid_input_with_spaces(self):
        self.assertFalse(validate_input("user name"))

    def test_invalid_input_with_empty_string(self):
        self.assertFalse(validate_input(""))

    def test_invalid_input_with_hyphens(self):
        self.assertFalse(validate_input("user-name"))

    def test_valid_input_with_only_numbers(self):
        self.assertTrue(validate_input("123456"))

    def test_valid_input_with_only_letters(self):
        self.assertTrue(validate_input("username"))

    def test_invalid_input_with_mixed_special_characters(self):
        self.assertFalse(validate_input("user$name!"))

    def test_valid_input_with_mixed_case_letters(self):
        self.assertTrue(validate_input("UserName123"))
