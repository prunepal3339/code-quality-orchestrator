import re
import unittest

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

class TestValidateEmail(unittest.TestCase):

    def test_valid_email(self):
        result = validate_email('test.email@example.com')
        print(f"Test valid email 'test.email@example.com': {result}")
        self.assertTrue(result)

    def test_valid_email_with_digits(self):
        result = validate_email('user123@example.com')
        print(f"Test valid email 'user123@example.com': {result}")
        self.assertTrue(result)

    def test_valid_email_with_special_characters(self):
        result = validate_email('user+name@example.co.uk')
        print(f"Test valid email 'user+name@example.co.uk': {result}")
        self.assertTrue(result)

    def test_invalid_email_missing_at_symbol(self):
        result = validate_email('invalidemail.com')
        print(f"Test invalid email 'invalidemail.com': {result}")
        self.assertFalse(result)

    def test_invalid_email_double_at_symbol(self):
        result = validate_email('user@@example.com')
        print(f"Test invalid email 'user@@example.com': {result}")
        self.assertFalse(result)

    def test_invalid_email_missing_domain(self):
        result = validate_email('user@.com')
        print(f"Test invalid email 'user@.com': {result}")
        self.assertFalse(result)

    def test_invalid_email_multiple_dots_in_domain(self):
        result = validate_email('user@example..com')
        print(f"Test invalid email 'user@example..com': {result}")
        self.assertFalse(result)

    def test_invalid_email_missing_username(self):
        result = validate_email('@example.com')
        print(f"Test invalid email '@example.com': {result}")
        self.assertFalse(result)

    def test_invalid_email_special_characters_in_domain(self):
        result = validate_email('user@ex!ample.com')
        print(f"Test invalid email 'user@ex!ample.com': {result}")
        self.assertFalse(result)

    def test_invalid_email_short_tld(self):
        result = validate_email('user@example.c')
        print(f"Test invalid email 'user@example.c': {result}")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()