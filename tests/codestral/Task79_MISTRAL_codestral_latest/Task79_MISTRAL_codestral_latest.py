import unittest

from output.codestral.Task79_MISTRAL_codestral_latest import encrypt as encrypt
class TestEncryptFunction(unittest.TestCase):

    def test_encrypt_lowercase(self):
        self.assertEqual(encrypt('hello', 3), 'khoor')

    def test_encrypt_uppercase(self):
        self.assertEqual(encrypt('HELLO', 5), 'MJQQT')

    def test_encrypt_mixed_case(self):
        self.assertEqual(encrypt('HeLLo', 2), 'JgNNq')

    def test_encrypt_with_spaces(self):
        self.assertEqual(encrypt('hello world', 3), 'khoor zruog')

    def test_encrypt_with_non_alpha(self):
        self.assertEqual(encrypt('hello, world!', 1), 'ifmmp, xpsme!')

    def test_encrypt_key_zero(self):
        self.assertEqual(encrypt('hello', 0), 'hello')

    def test_encrypt_full_rotation(self):
        self.assertEqual(encrypt('abc', 26), 'abc')

    def test_encrypt_negative_key(self):
        self.assertEqual(encrypt('def', -3), 'abc')

    def test_encrypt_with_large_key(self):
        self.assertEqual(encrypt('abc', 30), 'efg')

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt('', 5), '')