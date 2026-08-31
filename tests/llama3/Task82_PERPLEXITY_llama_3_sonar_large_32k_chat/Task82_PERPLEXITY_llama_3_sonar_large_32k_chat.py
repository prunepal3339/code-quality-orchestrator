import hashlib
import unittest

from output.gtp4o.Task82_OPENAI_gpt_4o import compute_hash


class TestComputeHash(unittest.TestCase):

    def setUp(self):
        self.password = "mysecretpassword"
        self.salt = "mysalt"
        self.expected_hash = hashlib.sha256((self.password + self.salt).encode()).hexdigest()

    def test_compute_hash_standard(self):
        result = compute_hash(self.password, self.salt)
        self.assertEqual(result, self.expected_hash)

    def test_compute_hash_different_password(self):
        different_password = "anotherpassword"
        result = compute_hash(different_password, self.salt)
        different_hash = hashlib.sha256((different_password + self.salt).encode()).hexdigest()
        self.assertNotEqual(result, different_hash)

    def test_compute_hash_different_salt(self):
        different_salt = "diffsalt"
        result = compute_hash(self.password, different_salt)
        different_hash = hashlib.sha256((self.password + different_salt).encode()).hexdigest()
        self.assertNotEqual(result, different_hash)

    def test_compute_hash_empty_password(self):
        empty_password = ""
        result = compute_hash(empty_password, self.salt)
        empty_password_hash = hashlib.sha256((empty_password + self.salt).encode()).hexdigest()
        self.assertEqual(result, empty_password_hash)

    def test_compute_hash_empty_salt(self):
        empty_salt = ""
        result = compute_hash(self.password, empty_salt)
        empty_salt_hash = hashlib.sha256((self.password + empty_salt).encode()).hexdigest()
        self.assertEqual(result, empty_salt_hash)

    def test_compute_hash_empty_password_and_salt(self):
        result = compute_hash("", "")
        empty_password_salt_hash = hashlib.sha256(("").encode()).hexdigest()
        self.assertEqual(result, empty_password_salt_hash)

    def test_compute_hash_long_password(self):
        long_password = "a" * 1000
        result = compute_hash(long_password, self.salt)
        long_password_hash = hashlib.sha256((long_password + self.salt).encode()).hexdigest()
        self.assertEqual(result, long_password_hash)

    def test_compute_hash_long_salt(self):
        long_salt = "b" * 1000
        result = compute_hash(self.password, long_salt)
        long_salt_hash = hashlib.sha256((self.password + long_salt).encode()).hexdigest()
        self.assertEqual(result, long_salt_hash)

    def test_compute_hash_special_characters(self):
        special_password = "!@#$%^&*()_+"
        special_salt = "~`<>?/|"
        result = compute_hash(special_password, special_salt)
        special_hash = hashlib.sha256((special_password + special_salt).encode()).hexdigest()
        self.assertEqual(result, special_hash)

    def test_compute_hash_case_sensitivity(self):
        different_case_password = "MySecretPassword"
        result = compute_hash(different_case_password, self.salt)
        different_case_hash = hashlib.sha256((different_case_password + self.salt).encode()).hexdigest()
        self.assertNotEqual(result, different_case_hash)

if __name__ == '__main__':
        unittest.main()