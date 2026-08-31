import re
import unittest


def validate_email(input):
    # Email validation
    email_pattern = r'^[\w\\.-]+@[\w\.-]+\.\w+$'
    email = input
    if re.match(email_pattern, email):
        return "Valid email"
    else:
        return  "Invalid email"
def validate_phone(input):
    # Phone number validation (US format)
    phone_pattern = r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$'
    phone = input
    if re.match(phone_pattern, phone):
        return "Valid phone number"
    else:
        return "Invalid phone number"
def validate_password(input):
    # Password validation (at least 8 characters, 1 uppercase, 1 lowercase, 1 digit)
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    password = input
    if re.match(password_pattern, password):
        return "Valid password"
    else:
        return "Invalid password"


class TestValidationFunctions(unittest.TestCase):

    # Test cases for validate_email
    def test_valid_email(self):
        self.assertEqual(validate_email("test@example.com"), "Valid email")

    def test_invalid_email(self):
        self.assertEqual(validate_email("invalid-email"), "Invalid email")

    def test_valid_email_with_subdomain(self):
        self.assertEqual(validate_email("user@domain.co.uk"), "Valid email")

    def test_invalid_email_missing_username(self):
        self.assertEqual(validate_email("user@.com"), "Invalid email")

    def test_invalid_email_missing_at_symbol(self):
        self.assertEqual(validate_email("userdomain.com"), "Invalid email")

    # Test cases for validate_phone
    def test_valid_phone(self):
        self.assertEqual(validate_phone("(123) 456-7890"), "Valid phone number")

    def test_invalid_phone_with_letters(self):
        self.assertEqual(validate_phone("123-abc-7890"), "Invalid phone number")

    def test_valid_phone_with_dashes(self):
        self.assertEqual(validate_phone("123-456-7890"), "Valid phone number")

    def test_invalid_phone_with_extra_digits(self):
        self.assertEqual(validate_phone("123-456-78901"), "Invalid phone number")

    # Test cases for validate_password
    def test_valid_password(self):
        self.assertEqual(validate_password("Password1"), "Valid password")

    def test_invalid_password_no_uppercase(self):
        self.assertEqual(validate_password("password1"), "Invalid password")

    def test_invalid_password_no_digit(self):
        self.assertEqual(validate_password("Password"), "Invalid password")

    def test_invalid_password_too_short(self):
        self.assertEqual(validate_password("Pass1"), "Invalid password")

if __name__ == '__main__':
    unittest.main()
