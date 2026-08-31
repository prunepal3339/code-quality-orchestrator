import unittest


def func(password) :
    if (len(password) >= 8 and
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password)):
        return True
    else:
        return False


class TestPasswordStrength(unittest.TestCase):

    def test_short_password(self):
        self.assertFalse(func("Ab1"))

    def test_no_uppercase(self):
        self.assertFalse(func("abcdefgh1"))

    def test_no_lowercase(self):
        self.assertFalse(func("ABCDEF1"))

    def test_no_digit(self):
        self.assertFalse(func("Abcdefgh"))

    def test_valid_password(self):
        self.assertTrue(func("Abcdefg1"))

    def test_password_exactly_8_chars(self):
        self.assertTrue(func("A1bcdefg"))

    def test_password_with_special_characters(self):
        self.assertTrue(func("A1@bcdEf"))

    def test_all_uppercase(self):
        self.assertFalse(func("ABCDEFGHI"))

    def test_all_lowercase(self):
        self.assertFalse(func("abcdefgh"))

    def test_password_with_spaces(self):
        self.assertTrue(func("A1 bcdEf"))

if __name__ == '__main__':
    unittest.main()