import unittest
from unittest.mock import patch
from io import StringIO

# Assuming the code snippet is encapsulated in a function named `process_integer`
def process_integer():
    try:
        number = int(input("Enter an integer: "))
        print("The entered integer is:", number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

class TestProcessInteger(unittest.TestCase):

    @patch('builtins.input', return_value='10')
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_integer(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("The entered integer is: 10", output)

    @patch('builtins.input', return_value='-5')
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_negative_integer(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("The entered integer is: -5", output)

    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_zero_integer(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("The entered integer is: 0", output)

    @patch('builtins.input', return_value='3.14')
    @patch('sys.stdout', new_callable=StringIO)
    def test_float_input(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter an integer.", output)

    @patch('builtins.input', return_value='abc')
    @patch('sys.stdout', new_callable=StringIO)
    def test_string_input(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter an integer.", output)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_input(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter an integer.", output)

    @patch('builtins.input', return_value='1000000')
    @patch('sys.stdout', new_callable=StringIO)
    def test_large_integer_input(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("The entered integer is: 1000000", output)

    @patch('builtins.input', return_value='-1000000')
    @patch('sys.stdout', new_callable=StringIO)
    def test_large_negative_integer_input(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("The entered integer is: -1000000", output)

    @patch('builtins.input', return_value='1e6')
    @patch('sys.stdout', new_callable=StringIO)
    def test_exponential_input(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter an integer.", output)

    @patch('builtins.input', return_value='10.0')
    @patch('sys.stdout', new_callable=StringIO)
    def test_float_input_with_decimal(self, mock_stdout, mock_input):
        process_integer()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter an integer.", output)

if __name__ == '__main__':
    unittest.main()
