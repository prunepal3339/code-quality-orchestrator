import unittest
from unittest.mock import patch
from io import StringIO

# Assuming the provided code snippet is encapsulated in a function named `calculate`
def calculate():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                exit()
        else:
            print("Error: Invalid operation!")
            exit()

        print("Result:", result)
    except ValueError:
        print("Error: Invalid input!")

class TestCalculate(unittest.TestCase):

    @patch('builtins.input', side_effect=['10', '5', '+'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition(self, mock_stdout, mock_input):
        calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 15.0", output)

    @patch('builtins.input', side_effect=['10', '5', '-'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtraction(self, mock_stdout, mock_input):
        calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 5.0", output)

    @patch('builtins.input', side_effect=['10', '5', '*'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication(self, mock_stdout, mock_input):
        calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 50.0", output)

    @patch('builtins.input', side_effect=['10', '5', '/'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division(self, mock_stdout, mock_input):
        calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 2.0", output)

    @patch('builtins.input', side_effect=['10', '0', '/'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_by_zero(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Division by zero!", output)

    @patch('builtins.input', side_effect=['10', '5', 'invalid'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_operation(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Invalid operation!", output)

    @patch('builtins.input', side_effect=['a', '5', '+'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_first_number(self, mock_stdout, mock_input):
        calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Invalid input!", output)

    @patch('builtins.input', side_effect=['10', 'b', '+'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_second_number(self, mock_stdout, mock_input):
        calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Invalid input!", output)

    @patch('builtins.input', side_effect=['10', '5', '/'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_float_result(self, mock_stdout, mock_input):
        calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 2.0", output)

    @patch('builtins.input', side_effect=['10', '2.5', '*'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication_float(self, mock_stdout, mock_input):
        calculate()
        output = mock_stdout.getvalue()
        self.assertIn("Result: 25.0", output)

if __name__ == '__main__':
    unittest.main()
