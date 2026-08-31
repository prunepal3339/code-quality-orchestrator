import os
import unittest
from output.gemini.Task52_GEMINI_gemini_1_5_pro_001 import *


class TestEncryptionFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.key_file = "secret.key"
        cls.test_file = "test.txt"
        cls.original_content = b"This is a test file content."

        # Create a test file with original content
        with open(cls.test_file, "wb") as f:
            f.write(cls.original_content)

    @classmethod
    def tearDownClass(cls):
        # Remove files after tests
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
        if os.path.exists(cls.key_file):
            os.remove(cls.key_file)

    def test_generate_key(self):
        generate_key()
        self.assertTrue(os.path.exists(self.key_file), "Key file should be created.")

    def test_load_key(self):
        generate_key()
        key = load_key()
        self.assertEqual(len(key), 44, "Key should be 44 bytes long.")

    def test_encrypt_decrypt_file(self):
        generate_key()
        key = load_key()

        # Encrypt the file
        encrypt_file(self.test_file, key)
        with open(self.test_file, "rb") as f:
            encrypted_content = f.read()

        self.assertNotEqual(encrypted_content, self.original_content, "File content should be encrypted.")

        # Decrypt the file
        decrypt_file(self.test_file, key)
        with open(self.test_file, "rb") as f:
            decrypted_content = f.read()

        self.assertEqual(decrypted_content, self.original_content, "File content should be decrypted correctly.")

if __name__ == "__main__":
    unittest.main()