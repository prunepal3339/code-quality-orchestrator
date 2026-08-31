import os
import unittest
from output.codestral.Task52_MISTRAL_codestral_latest import *





class TestFileEncryption(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a temporary file and key for testing."""
        cls.test_file_path = 'test_file.txt'
        cls.encrypted_file_path = cls.test_file_path + '.enc'
        cls.decrypted_file_path = cls.test_file_path + '.dec'
        cls.key = get_random_bytes(16)  # AES key must be 16, 24, or 32 bytes long

        # Create a temporary file with some data
        with open(cls.test_file_path, 'wb') as f:
            f.write(b'This is a test.')

    @classmethod
    def tearDownClass(cls):
        """Clean up files created during the tests."""
        for file_path in [cls.test_file_path, cls.encrypted_file_path, cls.decrypted_file_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_encrypt_file(self):
        """Test encryption of a file."""
        encrypt_file(self.key, self.test_file_path)
        self.assertTrue(os.path.exists(self.encrypted_file_path))

        # Verify the encrypted file is not the same as the original file
        with open(self.test_file_path, 'rb') as f:
            original_data = f.read()
        with open(self.encrypted_file_path, 'rb') as f:
            encrypted_data = f.read()
        self.assertNotEqual(original_data, encrypted_data)

    def test_decrypt_file(self):
        """Test decryption of a file."""
        encrypt_file(self.key, self.test_file_path)
        decrypt_file(self.key, self.encrypted_file_path, self.decrypted_file_path)

        # Verify the decrypted file matches the original file
        with open(self.test_file_path, 'rb') as f:
            original_data = f.read()
        with open(self.decrypted_file_path, 'rb') as f:
            decrypted_data = f.read()
        self.assertEqual(original_data, decrypted_data)

    def test_decrypt_non_existent_file(self):
        """Test decryption with a non-existent encrypted file."""
        with self.assertRaises(FileNotFoundError):
            decrypt_file(self.key, 'non_existent_file.enc', 'output.dec')

    def test_encrypt_non_existent_file(self):
        """Test encryption with a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            encrypt_file(self.key, 'non_existent_file.txt')

if __name__ == '__main__':
    unittest.main()