import hashlib
import unittest
from output.gemini.Task82_GEMINI_gemini_1_5_pro_001 import hash_password

class TestHashPassword(unittest.TestCase):

  def setUp(self):
    # Setting up common values for the tests
    self.password = "my_password"
    self.salt = b'salt_'
    self.expected_hash = hashlib.sha256(self.salt + self.password.encode('utf-8')).hexdigest()

  def test_hash_password_standard_case(self):
    result = hash_password(self.password, self.salt)
    self.assertEqual(result, self.expected_hash)

  def test_hash_password_empty_password(self):
    result = hash_password("", self.salt)
    expected_hash = hashlib.sha256(self.salt + "".encode('utf-8')).hexdigest()
    self.assertEqual(result, expected_hash)

  def test_hash_password_empty_salt(self):
    result = hash_password(self.password, b"")
    expected_hash = hashlib.sha256("".encode('utf-8') + self.password.encode('utf-8')).hexdigest()
    self.assertEqual(result, expected_hash)

  def test_hash_password_empty_password_and_salt(self):
    result = hash_password("", b"")
    expected_hash = hashlib.sha256("".encode('utf-8') + "".encode('utf-8')).hexdigest()
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
    expected_hash = hashlib.sha256(b"s@lt#" + "passw@rd!$".encode('utf-8')).hexdigest()
    self.assertEqual(result, expected_hash)

  # def test_hash_password_with_unicode_characters(self):
  #   result = hash_password("p@sswørd", b"råndøm$alt")
  #   expected_hash = hashlib.sha256(b"råndøm$alt" + "p@sswørd".encode('utf-8')).hexdigest()
  #   self.assertEqual(result, expected_hash)

  def test_hash_password_long_string(self):
    long_password = "a" * 1000
    long_salt = b"b" * 1000
    result = hash_password(long_password, long_salt)
    expected_hash = hashlib.sha256(long_salt + long_password.encode('utf-8')).hexdigest()
    self.assertEqual(result, expected_hash)

if __name__ == '__main__':
  unittest.main()