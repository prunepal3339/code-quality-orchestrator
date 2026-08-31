import hashlib
import binascii
import unittest
from output.codestral.Task82_MISTRAL_codestral_latest import hash_password


class TestHashPassword(unittest.TestCase):

    def setUp(self):
        # Setting up common values for the tests
        self.password = "my_password"
        self.salt = b'salt_'
        self.expected_hash = binascii.hexlify(
            hashlib.pbkdf2_hmac('sha256', self.password.encode(), self.salt, 100000)
        )

    def test_hash_password_standard_case(self):
        result = hash_password(self.password, self.salt)
        self.assertEqual(result, self.expected_hash)

    def test_hash_password_empty_password(self):
        result = hash_password("", self.salt)
        expected_hash = binascii.hexlify(
            hashlib.pbkdf2_hmac('sha256', "".encode(), self.salt, 100000)
        )
        self.assertEqual(result, expected_hash)

    def test_hash_password_empty_salt(self):
        result = hash_password(self.password, b"")
        expected_hash = binascii.hexlify(
            hashlib.pbkdf2_hmac('sha256', self.password.encode(), b"", 100000)
        )
        self.assertEqual(result, expected_hash)

    def test_hash_password_empty_password_and_salt(self):
        result = hash_password("", b"")
        expected_hash = binascii.hexlify(
            hashlib.pbkdf2_hmac('sha256', "".encode(), b"", 100000)
        )
        self.assertEqual(result, expected_hash)

    def test_hash_password_different_password(self):
        result = hash_password("different_password", self.salt)
        self.assertNotEqual(result, self.expected_hash)

    def test_hash_password_different_salt(self):
        result = hash_password(self.password, b"different_salt")
        self.assertNotEqual(result, self.expected_hash)

    def test_hash_password_different_password_and_salt(self):
        result = hash_password("different_password", b"different_salt")
        self.assertNotEqual(result, self.expected_hash)

    def test_hash_password_with_special_characters(self):
        result = hash_password("passw@rd!$", b"s@lt#")
        expected_hash = binascii.hexlify(
            hashlib.pbkdf2_hmac('sha256', "passw@rd!$".encode(), b"s@lt#", 100000)
        )
        self.assertEqual(result, expected_hash)

    # def test_hash_password_with_unicode_characters(self):
    #     result = hash_password("p@sswørd", b"råndøm$alt")
    #     expected_hash = binascii.hexlify(
    #         hashlib.pbkdf2_hmac('sha256', "p@sswørd".encode(), b"råndøm$alt", 100000)
    #     )
    #     self.assertEqual(result, expected_hash)

    def test_hash_password_long_string(self):
        long_password = "a" * 1000
        long_salt = b"b" * 1000
        result = hash_password(long_password, long_salt)
        expected_hash = binascii.hexlify(
            hashlib.pbkdf2_hmac('sha256', long_password.encode(), long_salt, 100000)
        )
        self.assertEqual(result, expected_hash)

if __name__ == '__main__':
    unittest.main()