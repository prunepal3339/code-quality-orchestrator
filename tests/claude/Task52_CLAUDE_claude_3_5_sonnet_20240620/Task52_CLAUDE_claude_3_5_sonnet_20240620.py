import os
import unittest
from output.claude.Task52_CLAUDE_claude_3_5_sonnet_20240620 import generate_key, encrypt_file, decrypt_file

class TestFileCrypto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a temporary file and key for testing."""
        cls.test_file_path = 'test_file.txt'
        cls.encrypted_file_path = cls.test_file_path + '.encrypted'
        cls.key = generate_key()

        # Create a temporary file with some data
        with open(cls.test_file_path, 'wb') as f:
            f.write(b'This is a test.')

    @classmethod
    def tearDownClass(cls):
        """Clean up files created during the tests."""
        for file_path in [cls.test_file_path, cls.encrypted_file_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_encrypt_file(self):
        """Test encryption of a file."""
        encrypt_file(self.test_file_path, self.key)
        self.assertTrue(os.path.exists(self.encrypted_file_path))

        # Verify the encrypted file is not the same as the original file
        with open(self.test_file_path, 'rb') as f:
            original_data = f.read()
        with open(self.encrypted_file_path, 'rb') as f:
            encrypted_data = f.read()
        self.assertNotEqual(original_data, encrypted_data)


    def test_decrypt_non_existent_file(self):
        """Test decryption with a non-existent encrypted file."""
        with self.assertRaises(FileNotFoundError):
            decrypt_file('non_existent_file.encrypted', self.key)

    def test_encrypt_non_existent_file(self):
        """Test encryption with a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            encrypt_file('non_existent_file.txt', self.key)

if __name__ == '__main__':
    unittest.main()