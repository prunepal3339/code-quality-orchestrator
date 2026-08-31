import unittest

from output.gtp4o.Task109_OPENAI_gpt_4o import validate_input


class TestValidateInput(unittest.TestCase):

    def test_valid_input_with_letters_and_numbers(self):
        self.assertEqual(validate_input("abc123"), "Valid input")

    def test_valid_input_with_underscore(self):
        self.assertEqual(validate_input("user_name"), "Valid input")

    def test_invalid_input_with_special_characters(self):
        self.assertEqual(validate_input("user@name"), "Invalid input")

    def test_invalid_input_with_spaces(self):
        self.assertEqual(validate_input("user name"), "Invalid input")

    def test_invalid_input_with_empty_string(self):
        self.assertEqual(validate_input(""), "Invalid input")

    def test_invalid_input_with_hyphens(self):
        self.assertEqual(validate_input("user-name"), "Invalid input")

    def test_valid_input_with_only_numbers(self):
        self.assertEqual(validate_input("123456"), "Valid input")

    def test_valid_input_with_only_letters(self):
        self.assertEqual(validate_input("username"), "Valid input")

    def test_invalid_input_with_mixed_special_characters(self):
        self.assertEqual(validate_input("user$name!"), "Invalid input")

    def test_valid_input_with_mixed_case_letters(self):
        self.assertEqual(validate_input("UserName123"), "Valid input")

if __name__ == '__main__':
    unittest.main()