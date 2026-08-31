# Python

import unittest
from unittest.mock import patch
import getpass

# Dictionary to store user credentials
users = {"user1": "password1", "user2": "password2"}

def authenticate_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    if username in users and users[username] == password:
        return ("Authentication successful.")
    else:
        return ("Invalid username or password.")

class TestAuthenticateUser(unittest.TestCase):

    @patch('builtins.input', side_effect=['user1'])
    @patch('getpass.getpass', return_value='password1')
    def test_authentication_successful(self, mock_getpass, mock_input):
        result = authenticate_user()
        self.assertEqual(result, "Authentication successful.")

    @patch('builtins.input', side_effect=['user1'])
    @patch('getpass.getpass', return_value='wrongpassword')
    def test_authentication_failure_wrong_password(self, mock_getpass, mock_input):
        result = authenticate_user()
        self.assertEqual(result, "Invalid username or password.")

    @patch('builtins.input', side_effect=['nonexistent_user'])
    @patch('getpass.getpass', return_value='password1')
    def test_authentication_failure_nonexistent_user(self, mock_getpass, mock_input):
        result = authenticate_user()
        self.assertEqual(result, "Invalid username or password.")

    @patch('builtins.input', side_effect=['user2'])
    @patch('getpass.getpass', return_value='password2')
    def test_authentication_successful_another_user(self, mock_getpass, mock_input):
        result = authenticate_user()
        self.assertEqual(result, "Authentication successful.")

    @patch('builtins.input', side_effect=['user2'])
    @patch('getpass.getpass', return_value='password1')
    def test_authentication_failure_wrong_password_another_user(self, mock_getpass, mock_input):
        result = authenticate_user()
        self.assertEqual(result, "Invalid username or password.")

    @patch('builtins.input', side_effect=['user1'])
    @patch('getpass.getpass', return_value='')
    def test_authentication_failure_empty_password(self, mock_getpass, mock_input):
        result = authenticate_user()
        self.assertEqual(result, "Invalid username or password.")

    @patch('builtins.input', side_effect=['user1'])
    @patch('getpass.getpass', return_value='password1' * 10)  # Extremely long password
    def test_authentication_failure_long_password(self, mock_getpass, mock_input):
        result = authenticate_user()
        self.assertEqual(result, "Invalid username or password.")

    @patch('builtins.input', side_effect=['user1'])
    @patch('getpass.getpass', return_value='password1')
    def test_authentication_success_repeated_calls(self, mock_getpass, mock_input):
        result1 = authenticate_user()

        self.assertEqual(result1, "Authentication successful.")


    @patch('builtins.input', side_effect=['user2'])
    @patch('getpass.getpass', return_value='password2')
    def test_authentication_success_repeated_calls_different_user(self, mock_getpass, mock_input):
        result1 = authenticate_user()

        self.assertEqual(result1, "Authentication successful.")


    @patch('builtins.input', side_effect=['user1'])
    @patch('getpass.getpass', return_value='wrongpassword')
    def test_authentication_failure_wrong_password_repeated_calls(self, mock_getpass, mock_input):
        result1 = authenticate_user()
        self.assertEqual(result1, "Invalid username or password.")


if __name__ == "__main__":
    unittest.main()



