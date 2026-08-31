import hashlib
import unittest

from output.claude.Task82_CLAUDE_claude_3_5_sonnet_20240620 import hash_password

class TestHashPassword(unittest.TestCase):

    def setUp(self):
        # Setting up common values for the tests
        self.password = "mypassword123"
        self.salt = "randomsalt"
        self.expected_hash = hashlib.sha256((self.password + self.salt).encode()).hexdigest()

    def test_hash_password_standard_case(self):
        result = hash_password(self.password, self.salt)
        self.assertEqual(result, self.expected_hash)

    def test_hash_password_empty_password(self):
        result = hash_password("", self.salt)
        self.assertEqual(result, hashlib.sha256(self.salt.encode()).hexdigest())

    def test_hash_password_empty_salt(self):
        result = hash_password(self.password, "")
        self.assertEqual(result, hashlib.sha256(self.password.encode()).hexdigest())

    def test_hash_password_empty_password_and_salt(self):
        result = hash_password("", "")
        self.assertEqual(result, hashlib.sha256("".encode()).hexdigest())

    def test_hash_password_different_password(self):
        result = hash_password("differentpassword", self.salt)
        self.assertNotEqual(result, self.expected_hash)

    def test_hash_password_different_salt(self):
        result = hash_password(self.password, "differentsalt")
        self.assertNotEqual(result, self.expected_hash)

    def test_hash_password_different_password_and_salt(self):
        result = hash_password("differentpassword", "differentsalt")
        self.assertNotEqual(result, self.expected_hash)

    def test_hash_password_with_special_characters(self):
        result = hash_password("passw@rd!$", "s@lt#")
        expected_hash = hashlib.sha256("passw@rd!$s@lt#".encode()).hexdigest()
        self.assertEqual(result, expected_hash)

    def test_hash_password_with_unicode_characters(self):
        result = hash_password("p@sswørd", "råndøm$alt")
        expected_hash = hashlib.sha256("p@sswørdråndøm$alt".encode()).hexdigest()
        self.assertEqual(result, expected_hash)

    def test_hash_password_long_string(self):
        long_password = "a" * 1000
        long_salt = "b" * 1000
        result = hash_password(long_password, long_salt)
        expected_hash = hashlib.sha256((long_password + long_salt).encode()).hexdigest()
        self.assertEqual(result, expected_hash)

if __name__ == '__main__':
    unittest.main()