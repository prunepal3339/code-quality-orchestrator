import unittest
from io import StringIO
from unittest.mock import patch


class TestSquareCalculation(unittest.TestCase):

    def run_test_with_input(self, inputs, expected_output):
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new=StringIO()) as mock_stdout:
            # Run the provided code
            user_input = input("Enter a number: ")
            try:
                number = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number.")
            else:
                print("You entered:", number)
                squared = number * number
                print("Square of the number:", squared)

            # Check output
            output = mock_stdout.getvalue().strip().split('\n')
            self.assertEqual(output, expected_output)

    def test_valid_input(self):
        self.run_test_with_input(['4'], [
            "You entered: 4",
            "Square of the number: 16"
        ])

    def test_invalid_input_then_valid(self):
        self.run_test_with_input(['foo', '3'], [
            "Invalid input. Please enter a number.",
            "You entered: 3",
            "Square of the number: 9"
        ])

    def test_multiple_invalid_inputs_then_valid(self):
        self.run_test_with_input(['abc', 'xyz', '5'], [
            "Invalid input. Please enter a number.",
            "Invalid input. Please enter a number.",
            "You entered: 5",
            "Square of the number: 25"
        ])

    def test_negative_number(self):
        self.run_test_with_input(['-3'], [
            "You entered: -3",
            "Square of the number: 9"
        ])

    def test_zero(self):
        self.run_test_with_input(['0'], [
            "You entered: 0",
            "Square of the number: 0"
        ])

    def test_large_number(self):
        self.run_test_with_input(['12345'], [
            "You entered: 12345",
            "Square of the number: 152399025"
        ])

    def test_decimal_number(self):
        self.run_test_with_input(['2.5'], [
            "Invalid input. Please enter a number.",
            "You entered: 2.5",
            "Square of the number: 6.25"
        ])

    def test_empty_input(self):
        self.run_test_with_input([''], [
            "Invalid input. Please enter a number.",
            "You entered: 0",
            "Square of the number: 0"
        ])

    def test_spaces_input(self):
        self.run_test_with_input(['   7   '], [
            "You entered: 7",
            "Square of the number: 49"
        ])

    def test_special_characters_input(self):
        self.run_test_with_input(['@#!'], [
            "Invalid input. Please enter a number.",
            "You entered: 0",
            "Square of the number: 0"
        ])

if __name__ == '__main__':
    unittest.main()