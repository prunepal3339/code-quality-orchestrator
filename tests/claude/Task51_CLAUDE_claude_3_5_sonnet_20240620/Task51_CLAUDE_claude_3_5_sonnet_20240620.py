from output.claude.Task51_CLAUDE_claude_3_5_sonnet_20240620 import encrypt as encrypt
import unittest

class TestEncryptFunction(unittest.TestCase):

    def test_basic_encryption(self):
        self.assertEqual(encrypt("abc", 3), "def")

    def test_encryption_with_uppercase(self):
        self.assertEqual(encrypt("ABC", 3), "DEF")

    def test_encryption_with_mixed_case(self):
        self.assertEqual(encrypt("aBc", 2), "cDe")

    def test_encryption_with_non_alpha_characters(self):
        self.assertEqual(encrypt("a b-c", 5), "f g-h")

    def test_encryption_with_large_shift_value(self):
        self.assertEqual(encrypt("xyz", 30), "bcd")

    def test_encryption_with_negative_shift_value(self):
        self.assertEqual(encrypt("def", -3), "abc")

    def test_encryption_with_shift_value_zero(self):
        self.assertEqual(encrypt("hello", 0), "hello")

    def test_encryption_with_shift_value_26(self):
        self.assertEqual(encrypt("xyz", 26), "xyz")

    def test_encryption_empty_string(self):
        self.assertEqual(encrypt("", 5), "")

    def test_encryption_non_alpha_characters_only(self):
        self.assertEqual(encrypt("1234!@#$", 4), "1234!@#$")

if __name__ == "__main__":
    unittest.main()