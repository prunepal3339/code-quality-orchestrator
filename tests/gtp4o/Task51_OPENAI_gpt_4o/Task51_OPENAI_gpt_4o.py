import unittest
from output.gtp4o.Task51_OPENAI_gpt_4o import encrypt as encrypt

class TestEncryptFunction(unittest.TestCase):

    def test_basic_encryption(self):
        self.assertEqual(encrypt("abc"), "bcd")

    def test_encryption_with_uppercase(self):
        self.assertEqual(encrypt("ABC"), "BCD")

    def test_encryption_with_mixed_case(self):
        self.assertEqual(encrypt("aBc"), "bCd")

    def test_encryption_with_non_alpha_characters(self):
        self.assertEqual(encrypt("a b-c"), "b c-d")

    def test_encryption_with_wrap_around(self):
        self.assertEqual(encrypt("xyz"), "yza")

    def test_encryption_with_uppercase_wrap_around(self):
        self.assertEqual(encrypt("XYZ"), "YZA")

    def test_encryption_with_mixed_case_wrap_around(self):
        self.assertEqual(encrypt("XyZ"), "YzA")

    def test_encryption_empty_string(self):
        self.assertEqual(encrypt(""), "")

    def test_encryption_with_numbers(self):
        self.assertEqual(encrypt("1234"), "1234")

    def test_encryption_with_special_characters(self):
        self.assertEqual(encrypt("!@#$"), "!@#$")

if __name__ == "__main__":
    unittest.main()