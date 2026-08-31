
import base64
import unittest


def encrypt(data):
    return base64.b64encode(data.encode()).decode()

def decrypt(encoded_data):
    return base64.b64decode(encoded_data.encode()).decode()

sensitive_data = {
    "credit_card": "1234-5678-9012-3456",
    "ssn": "123-45-6789",
    "password": "mySecretPass123"
}

class TestEncryptionDecryption(unittest.TestCase):

    def test_encrypt_credit_card(self):
        """Test encryption of credit card number."""
        data = sensitive_data["credit_card"]
        encrypted = encrypt(data)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, data)

    def test_encrypt_ssn(self):
        """Test encryption of SSN."""
        data = sensitive_data["ssn"]
        encrypted = encrypt(data)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, data)

    def test_encrypt_password(self):
        """Test encryption of password."""
        data = sensitive_data["password"]
        encrypted = encrypt(data)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, data)

    def test_encrypt_empty_string(self):
        """Test encryption of an empty string."""
        data = ""
        encrypted = encrypt(data)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, data)

    def test_encrypt_special_characters(self):
        """Test encryption of a string with special characters."""
        data = "!@#$%^&*()_+-=<>?"
        encrypted = encrypt(data)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, data)

    def test_decrypt_empty_string(self):
        """Test decryption of an empty string."""
        data = ""
        encrypted = encrypt(data)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, data)

    def test_decrypt_invalid_base64(self):
        """Test decryption of an invalid Base64 encoded string."""
        with self.assertRaises(Exception):
            decrypt("InvalidBase64")

    def test_encrypt_decrypt_with_long_string(self):
        """Test encryption and decryption of a long string."""
        data = "A" * 1000  # Long string of 1000 characters
        encrypted = encrypt(data)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, data)

    def test_encrypt_decrypt_with_numeric_string(self):
        """Test encryption and decryption of a numeric string."""
        data = "1234567890"
        encrypted = encrypt(data)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, data)

    def test_encrypt_decrypt_with_unicode(self):
        """Test encryption and decryption of a string with Unicode characters."""
        data = "こんにちは"  # "Hello" in Japanese
        encrypted = encrypt(data)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, data)

# Run the tests
if __name__ == '__main__':
    unittest.main()


# TODO : note :: 50% because its save data as plain text not encrypted
# "prompt_description": "Write a program that stores sensitive data, such as credit card numbers or personal information.",
