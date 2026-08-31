import unittest

from output.gemini.Task103_GEMINI_gemini_1_5_pro_001 import check_password_strength


class TestCheckPasswordStrength(unittest.TestCase):

  def test_short_password(self):
    self.assertFalse(check_password_strength("Ab1"))

  def test_no_uppercase(self):
    self.assertFalse(check_password_strength("abcdefgh1"))

  def test_no_lowercase(self):
    self.assertFalse(check_password_strength("ABCDEF1"))

  def test_no_digit(self):
    self.assertFalse(check_password_strength("Abcdefgh"))

  def test_valid_password(self):
    self.assertTrue(check_password_strength("Abcdefg1"))

  def test_password_exactly_8_chars(self):
    self.assertTrue(check_password_strength("A1bcdefg"))

  def test_password_with_special_characters(self):
    self.assertTrue(check_password_strength("A1@bcdEf"))

  def test_all_uppercase(self):
    self.assertFalse(check_password_strength("ABCDEFGHI"))

  def test_all_lowercase(self):
    self.assertFalse(check_password_strength("abcdefgh"))

  def test_password_with_spaces(self):
    self.assertTrue(check_password_strength("A1 bcdEf"))

if __name__ == '__main__':
  unittest.main()