import unittest

from output.llama3.Task79_PERPLEXITY_llama_3_sonar_large_32k_chat import *

class TestEncryptMessage(unittest.TestCase):

    def test_encryption_basic(self):
        message = "Hello, World!"
        key = 3
        encrypted = encrypt_message(message, key)
        self.assertEqual(encrypted, "Khoor, Zruog!")

    def test_encryption_empty_message(self):
        message = ""
        key = 5
        encrypted = encrypt_message(message, key)
        self.assertEqual(encrypted, "")

    def test_encryption_special_characters(self):
        message = "!@#$%^&*()_+-=~`"
        key = 7
        encrypted = encrypt_message(message, key)
        self.assertEqual(encrypted, "!@#$%^&*()_+-=~`")

    def test_encryption_long_message(self):
        message = "a" * 1000
        key = 10
        encrypted = encrypt_message(message, key)
        self.assertEqual(encrypted, "k" * 1000)

    def test_encryption_diff_key(self):
        message = "Different key test"
        key1 = 5
        key2 = 10
        encrypted1 = encrypt_message(message, key1)
        encrypted2 = encrypt_message(message, key2)
        self.assertNotEqual(encrypted1, encrypted2)

    def test_encryption_same_message_diff_keys(self):
        message = "Message with different keys"
        key1 = 3
        key2 = 7
        encrypted1 = encrypt_message(message, key1)
        encrypted2 = encrypt_message(message, key2)
        self.assertNotEqual(encrypted1, encrypted2)

    def test_encryption_invalid_key(self):
        message = "Key test"
        key = -1
        encrypted = encrypt_message(message, key)
        self.assertEqual(encrypted, "Jdws uvd")

    def test_encryption_unicode_message(self):
        message = "こんにちは世界"  # Japanese for "Hello, World"
        key = 4
        encrypted = encrypt_message(message, key)
        self.assertEqual(encrypted, "こんにちは世界")  # Unicode chars remain unchanged

    def test_encryption_key_with_spaces(self):
        message = "Key with spaces"
        key = 15
        encrypted = encrypt_message(message, key)
        self.assertEqual(encrypted, "Pth lzsl xhfw")

    def test_encryption_message_with_non_ascii(self):
        message = "Café Münsterländer"
        key = 8
        encrypted = encrypt_message(message, key)
        self.assertEqual(encrypted, "Kíísh Vwázsákpíh")

if __name__ == '__main__':
    unittest.main()