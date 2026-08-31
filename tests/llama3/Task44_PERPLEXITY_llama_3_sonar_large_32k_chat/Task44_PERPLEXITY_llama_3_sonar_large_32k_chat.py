import unittest
from io import StringIO
from unittest.mock import patch


def get_user_input(prompt):
    while True:
        try:
            return input(prompt)
        except EOFError:
            print("Invalid input. Please try again.")

def validate_input(input_str):
    if not input_str.isalpha():
        raise ValueError("Input should only contain alphabets")

def main():
    input_str = get_user_input("Enter a string: ")
    try:
        validate_input(input_str)
        print("Input is valid")
        print("Upper case: ", input_str.upper())
        print("Lower case: ", input_str.lower())
    except ValueError as e:
        print("Error: ", str(e))

class TestStringValidation(unittest.TestCase):

    def run_test_with_input(self, inputs, expected_output):
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new=StringIO()) as mock_stdout:
            # Run the provided code
            def get_user_input(prompt):
                while True:
                    try:
                        return input(prompt)
                    except EOFError:
                        print("Invalid input. Please try again.")

            def validate_input(input_str):
                if not input_str.isalpha():
                    raise ValueError("Input should only contain alphabets")

            def main():
                input_str = get_user_input("Enter a string: ")
                try:
                    validate_input(input_str)
                    print("Input is valid")
                    print("Upper case: ", input_str.upper())
                    print("Lower case: ", input_str.lower())
                except ValueError as e:
                    print("Error: ", str(e))

            main()

            # Check output
            output = mock_stdout.getvalue().strip().split('\n')
            self.assertEqual(output, expected_output)

    def test_valid_input(self):
        self.run_test_with_input(['hello'], [
            "Input is valid",
            "Upper case: HELLO",
            "Lower case: hello"
        ])

    def test_invalid_input_contains_numbers(self):
        self.run_test_with_input(['hello123'], [
            "Error:  Input should only contain alphabets"
        ])

    def test_invalid_input_contains_special_characters(self):
        self.run_test_with_input(['hello@'], [
            "Error:  Input should only contain alphabets"
        ])

    def test_empty_input(self):
        self.run_test_with_input([''], [
            "Error:  Input should only contain alphabets"
        ])

    def test_valid_input_all_uppercase(self):
        self.run_test_with_input(['WORLD'], [
            "Input is valid",
            "Upper case: WORLD",
            "Lower case: world"
        ])

    def test_valid_input_with_spaces(self):
        self.run_test_with_input(['Hello World'], [
            "Error:  Input should only contain alphabets"
        ])

    def test_valid_input_with_mixed_case(self):
        self.run_test_with_input(['HeLLo'], [
            "Input is valid",
            "Upper case: HELLO",
            "Lower case: hello"
        ])

    def test_valid_input_with_non_alpha_characters(self):
        self.run_test_with_input(['hello@world'], [
            "Error:  Input should only contain alphabets"
        ])

    def test_valid_input_with_multiple_invalid_entries(self):
        self.run_test_with_input(['123abc', 'validInput'], [
            "Error:  Input should only contain alphabets",
            "Input is valid",
            "Upper case: VALIDINPUT",
            "Lower case: validinput"
        ])

    def test_input_with_newline_character(self):
        self.run_test_with_input(['hello\n'], [
            "Input is valid",
            "Upper case: HELLO",
            "Lower case: hello"
        ])

if __name__ == '__main__':
    unittest.main()