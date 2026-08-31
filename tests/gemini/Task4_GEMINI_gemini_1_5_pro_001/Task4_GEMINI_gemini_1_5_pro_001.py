from output.gemini.Task4_GEMINI_gemini_1_5_pro_001 import is_isogram as isIsogram

import unittest

class TestIsogram(unittest.TestCase):

  def test_case1(self):
    self.assertTrue(isIsogram("Dermatoglyphics"))  # Basic isogram test

  def test_case2(self):
    self.assertTrue(isIsogram("isogram"))  # All lowercase isogram

  def test_case3(self):
    self.assertFalse(isIsogram("moOse"))  # Case-insensitive repeating letter

  def test_case4(self):
    self.assertFalse(isIsogram("aba"))  # Repeating letter

  def test_case5(self):
    self.assertTrue(isIsogram("Machine"))  # Mixed case isogram

  def test_case6(self):
    self.assertTrue(isIsogram(""))  # Edge case: Empty string

  def test_case7(self):
    self.assertFalse(isIsogram("Alphabet"))  # No repeating letters, mixed case

  def test_case8(self):
    self.assertFalse(isIsogram("letter"))  # Consecutive repeating letter

  def test_case9(self):
    self.assertFalse(isIsogram("Bookkeeper"))  # Multiple repeating letters

  def test_case10(self):
    self.assertFalse(isIsogram("Thumbscrew-japingly"))  # Complex isogram with hyphen (considered as part of the string)

if __name__ == '__main__':
  unittest.main()

