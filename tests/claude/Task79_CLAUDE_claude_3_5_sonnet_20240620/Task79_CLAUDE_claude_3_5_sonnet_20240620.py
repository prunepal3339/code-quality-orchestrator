import unittest

from output.claude.Task79_CLAUDE_claude_3_5_sonnet_20240620 import encrypt_message
class TestEncryptMessage(unittest.TestCase):

    def test_basic_encryption(self):
        result = encrypt_message("HELLO", 3)
        self.assertEqual(result, "KHOOR")  # Change as per the cipher generated for key=3

    def test_encryption_with_spaces(self):
        result = encrypt_message("HELLO WORLD", 5)
        self.assertEqual(result, "QNUXZ DMJFZ")  # Expected cipher output for key=5

    def test_encryption_with_special_characters(self):
        result = encrypt_message("HELLO, WORLD!", 2)
        self.assertEqual(result, "RDSSV, UFSVF!")  # Expected cipher output for key=2

    def test_empty_message(self):
        result = encrypt_message("", 10)
        self.assertEqual(result, "")  # Empty string should return empty

    def test_encryption_with_numbers(self):
        result = encrypt_message("HELLO123", 4)
        self.assertEqual(result, "GDKKN123")  # Non-alphabet characters are preserved

    def test_same_key_produces_same_output(self):
        result1 = encrypt_message("PYTHON", 6)
        result2 = encrypt_message("PYTHON", 6)
        self.assertEqual(result1, result2)  # Same key should produce same output

    def test_different_key_produces_different_output(self):
        result1 = encrypt_message("PYTHON", 6)
        result2 = encrypt_message("PYTHON", 8)
        self.assertNotEqual(result1, result2)  # Different keys should give different results

    def test_case_insensitive_encryption(self):
        result = encrypt_message("Python", 7)
        self.assertEqual(result, "DKSOQD")  # Encryption should be case-insensitive

    def test_key_affects_shuffling(self):
        result1 = encrypt_message("TEST", 9)
        result2 = encrypt_message("TEST", 10)
        self.assertNotEqual(result1, result2)  # Different keys should result in different ciphers

    def test_same_key_and_message_different_cases(self):
        result1 = encrypt_message("test", 11)
        result2 = encrypt_message("TEST", 11)
        self.assertEqual(result1, result2)  # Case difference should not affect output