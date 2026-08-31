import io
import unittest
from unittest.mock import patch

from output.llama3.Task109_PERPLEXITY_llama_3_sonar_large_32k_chat import validate_input


class TestValidateInput(unittest.TestCase):

    @patch('builtins.input', return_value="user123")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_username(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Valid username")

    @patch('builtins.input', return_value="username_with_underscores")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_username_with_underscores(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Valid username")

    @patch('builtins.input', return_value="usr")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_short_username(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Valid username")

    @patch('builtins.input', return_value="longusername123")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_long_username(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Valid username")

    @patch('builtins.input', return_value="us")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_username_too_short(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid username")

    @patch('builtins.input', return_value="username_is_too_long_for_validation")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_username_too_long(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid username")

    @patch('builtins.input', return_value="user!@#")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_username_with_special_characters(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid username")

    @patch('builtins.input', return_value="user name")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_username_with_spaces(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid username")

    @patch('builtins.input', return_value="user")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_username_min_length(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Valid username")

    @patch('builtins.input', return_value="username1234")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_username_max_length(self, mock_stdout, mock_input):
        validate_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Valid username")

if __name__ == '__main__':
    unittest.main()