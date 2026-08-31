import re
import unittest

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


class TestValidateEmail(unittest.TestCase):

    def test_valid_email(self):
        # Test a valid email
        self.assertTrue(validate_email('test.email@example.com'))

    def test_valid_email_with_digits(self):
        # Test a valid email with digits
        self.assertTrue(validate_email('user123@example.com'))

    def test_valid_email_with_special_characters(self):
        # Test a valid email with special characters
        self.assertTrue(validate_email('user+name@example.co.uk'))

    def test_invalid_email_missing_at_symbol(self):
        # Test an email without the @ symbol
        self.assertFalse(validate_email('invalidemail.com'))

    def test_invalid_email_double_at_symbol(self):
        # Test an email with double @ symbol
        self.assertFalse(validate_email('user@@example.com'))

    def test_invalid_email_missing_domain(self):
        # Test an email with missing domain part
        self.assertFalse(validate_email('user@.com'))

    def test_invalid_email_multiple_dots_in_domain(self):
        # Test an email with multiple consecutive dots in the domain
        self.assertFalse(validate_email('user@example..com'))

    def test_invalid_email_missing_username(self):
        # Test an email with missing username
        self.assertFalse(validate_email('@example.com'))

    def test_invalid_email_special_characters_in_domain(self):
        # Test an email with special characters in the domain part
        self.assertFalse(validate_email('user@ex!ample.com'))

    def test_invalid_email_short_tld(self):
        # Test an email with an invalid top-level domain
        self.assertFalse(validate_email('user@example.c'))

if __name__ == "__main__":
    unittest.main()