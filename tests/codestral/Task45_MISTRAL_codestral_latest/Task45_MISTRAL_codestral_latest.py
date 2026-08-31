import unittest
from unittest.mock import patch
from io import StringIO

# Assume the code snippet is defined in a function named `process_number`
def process_number():
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)
        result = number * 2
        return f"The result is: {result}"
    except ValueError:
        return "Invalid input. Please enter a number."

class TestProcessNumber(unittest.TestCase):

    @patch('builtins.input', return_value='10')
    def test_valid_input_positive(self, mock_input):
        result = process_number()
        self.assertEqual(result, "The result is: 20.0")

    @patch('builtins.input', return_value='-5')
    def test_valid_input_negative(self, mock_input):
        result = process_number()
        self.assertEqual(result, "The result is: -10.0")

    @patch('builtins.input', return_value='0')
    def test_valid_input_zero(self, mock_input):
        result = process_number()
        self.assertEqual(result, "The result is: 0.0")

    @patch('builtins.input', return_value='3.5')
    def test_valid_input_float(self, mock_input):
        result = process_number()
        self.assertEqual(result, "The result is: 7.0")

    @patch('builtins.input', return_value='abc')
    def test_invalid_input(self, mock_input):
        result = process_number()
        self.assertEqual(result, "Invalid input. Please enter a number.")

    @patch('builtins.input', return_value='')
    def test_empty_input(self, mock_input):
        result = process_number()
        self.assertEqual(result, "Invalid input. Please enter a number.")

    @patch('builtins.input', return_value='999999999999')
    def test_large_number_input(self, mock_input):
        result = process_number()
        self.assertEqual(result, "The result is: 1999999999998.0")

    @patch('builtins.input', return_value='1e10')
    def test_exponential_input(self, mock_input):
        result = process_number()
        self.assertEqual(result, "The result is: 20000000000.0")

    @patch('builtins.input', return_value='0.0001')
    def test_small_number_input(self, mock_input):
        result = process_number()
        self.assertEqual(result, "The result is: 0.0002")

    @patch('builtins.input', return_value='-0.0001')
    def test_small_negative_number_input(self, mock_input):
        result = process_number()
        self.assertEqual(result, "The result is: -0.0002")

if __name__ == '__main__':
    unittest.main()
