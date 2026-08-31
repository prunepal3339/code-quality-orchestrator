import unittest

from output.gtp4o.Task79_OPENAI_gpt_4o import encrypt_message
class TestEncryptMessage(unittest.TestCase):

    def setUp(self):
        self.secret_key = "thisisaverysecret"

    def test_encryption_basic(self):
        message = "Hello, World!"
        encrypted = encrypt_message(message, self.secret_key)
        self.assertIsInstance(encrypted, str)
        self.assertGreater(len(encrypted), 0)

    def test_encryption_empty_message(self):
        message = ""
        encrypted = encrypt_message(message, self.secret_key)
        self.assertIsInstance(encrypted, str)
        self.assertGreater(len(encrypted), 0)

    def test_encryption_special_characters(self):
        message = "!@#$%^&*()_+-=~`"
        encrypted = encrypt_message(message, self.secret_key)
        self.assertIsInstance(encrypted, str)
        self.assertGreater(len(encrypted), 0)

    def test_encryption_long_message(self):
        message = "a" * 1000
        encrypted = encrypt_message(message, self.secret_key)
        self.assertIsInstance(encrypted, str)
        self.assertGreater(len(encrypted), 0)

    def test_encryption_diff_key(self):
        diff_key = "anothersecretkey"
        message = "Different key test"
        encrypted1 = encrypt_message(message, self.secret_key)
        encrypted2 = encrypt_message(message, diff_key)
        self.assertNotEqual(encrypted1, encrypted2)

    def test_encryption_same_message_diff_keys(self):
        message = "Message with different keys"
        key1 = "keyonekeyonekeyone"
        key2 = "keytwokeytwokeytwo"
        encrypted1 = encrypt_message(message, key1)
        encrypted2 = encrypt_message(message, key2)
        self.assertNotEqual(encrypted1, encrypted2)

    def test_encryption_invalid_key_length(self):
        invalid_key = "shortkey"
        message = "Key length test"
        with self.assertRaises(ValueError):
            encrypt_message(message, invalid_key)

    def test_encryption_unicode_message(self):
        message = "こんにちは世界"  # Japanese for "Hello, World"
        encrypted = encrypt_message(message, self.secret_key)
        self.assertIsInstance(encrypted, str)
        self.assertGreater(len(encrypted), 0)

    def test_encryption_key_with_spaces(self):
        message = "Key with spaces"
        key_with_spaces = "key with spaces!"
        encrypted = encrypt_message(message, key_with_spaces)
        self.assertIsInstance(encrypted, str)
        self.assertGreater(len(encrypted), 0)

    def test_encryption_message_with_non_ascii(self):
        message = "Café Münsterländer"
        encrypted = encrypt_message(message, self.secret_key)
        self.assertIsInstance(encrypted, str)
        self.assertGreater(len(encrypted), 0)

if __name__ == '__main__':
    unittest.main()