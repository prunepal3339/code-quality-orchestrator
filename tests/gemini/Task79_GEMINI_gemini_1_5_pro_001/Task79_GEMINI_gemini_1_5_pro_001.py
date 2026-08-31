import unittest

from cryptography.fernet import Fernet
from output.gemini.Task79_GEMINI_gemini_1_5_pro_001 import encrypt_message as encrypt_message


class TestEncryptMessageFunction(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.key = Fernet.generate_key()  # Generate a key for testing
    cls.cipher = Fernet(cls.key)

  def test_encrypt_lowercase(self):
    message = 'hello'
    encrypted_message = encrypt_message(message, self.key)
    self.assertNotEqual(message, encrypted_message)

  def test_encrypt_uppercase(self):
    message = 'HELLO'
    encrypted_message = encrypt_message(message, self.key)
    self.assertNotEqual(message, encrypted_message)

  def test_encrypt_mixed_case(self):
    message = 'HeLLo'
    encrypted_message = encrypt_message(message, self.key)
    self.assertNotEqual(message, encrypted_message)

  def test_encrypt_with_spaces(self):
    message = 'hello world'
    encrypted_message = encrypt_message(message, self.key)
    self.assertNotEqual(message, encrypted_message)

  def test_encrypt_with_non_alpha(self):
    message = 'hello, world!'
    encrypted_message = encrypt_message(message, self.key)
    self.assertNotEqual(message, encrypted_message)

  def test_encrypt_empty_string(self):
    message = ''
    encrypted_message = encrypt_message(message, self.key)
    self.assertNotEqual(message, encrypted_message)

  def test_encrypt_different_keys(self):
    key2 = Fernet.generate_key()
    message = 'test'
    encrypted_message1 = encrypt_message(message, self.key)
    encrypted_message2 = encrypt_message(message, key2)
    self.assertNotEqual(encrypted_message1, encrypted_message2)

  def test_encrypt_invalid_key(self):
    with self.assertRaises(ValueError):
      # Using an invalid key (not a valid Fernet key)
      encrypt_message('test', 'invalidkey')

  def test_encrypt_key_length(self):
    # Ensure that the key is the correct length
    self.assertEqual(len(self.key), 44)

  def test_encrypt_with_large_message(self):
    message = 'a' * 10000  # Large message
    encrypted_message = encrypt_message(message, self.key)
    self.assertNotEqual(message, encrypted_message)