import unittest
from unittest.mock import patch
from io import StringIO

from output.claude.Task45_CLAUDE_claude_3_5_sonnet_20240620 import divide_numbers, main


class TestDivideNumbers(unittest.TestCase):

    def test_divide_numbers_valid(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertEqual(divide_numbers(-10, 2), -5)
        self.assertEqual(divide_numbers(0, 1), 0)

    def test_divide_numbers_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(10, 0)

    def test_divide_numbers_invalid_input(self):
        with self.assertRaises(TypeError):
            divide_numbers("10", "2")

    @patch('builtins.input', side_effect=['10', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_input(self, mock_stdout, mock_input):
        with patch('builtins.input', side_effect=['10', '2']):
            main()
        self.assertIn("Result: 5.0", mock_stdout.getvalue())
        self.assertIn("Program execution completed.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['10', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_zero_division(self, mock_stdout, mock_input):
        with patch('builtins.input', side_effect=['10', '0']):
            main()
        self.assertIn("Error: Cannot divide by zero.", mock_stdout.getvalue())
        self.assertIn("Program execution completed.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['a', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_invalid_input(self, mock_stdout, mock_input):
        with patch('builtins.input', side_effect=['a', '2']):
            main()
        self.assertIn("Error: Please enter valid numbers.", mock_stdout.getvalue())
        self.assertIn("Program execution completed.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['10', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_invalid_input(self, mock_stdout, mock_input):
        with patch('builtins.input', side_effect=['10', '2']):
            try:
                main()
            except Exception:
                pass
        self.assertIn("Result: 5.0", mock_stdout.getvalue())
        self.assertIn("Program execution completed.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['-10', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_negative_numbers(self, mock_stdout, mock_input):
        with patch('builtins.input', side_effect=['-10', '2']):
            main()
        self.assertIn("Result: -5.0", mock_stdout.getvalue())
        self.assertIn("Program execution completed.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_zero_numerator(self, mock_stdout, mock_input):
        with patch('builtins.input', side_effect=['0', '1']):
            main()
        self.assertIn("Result: 0.0", mock_stdout.getvalue())
        self.assertIn("Program execution completed.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['10', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_input_multiple_times(self, mock_stdout, mock_input):
        for _ in range(10):
            with patch('builtins.input', side_effect=['10', '2']):
                main()
        self.assertIn("Result: 5.0", mock_stdout.getvalue())
        self.assertIn("Program execution completed.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_small_numbers_zero_division(self, mock_stdout, mock_input):
        with patch('builtins.input', side_effect=['1', '0']):
            main()
        self.assertIn("Error: Cannot divide by zero.", mock_stdout.getvalue())
        self.assertIn("Program execution completed.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
