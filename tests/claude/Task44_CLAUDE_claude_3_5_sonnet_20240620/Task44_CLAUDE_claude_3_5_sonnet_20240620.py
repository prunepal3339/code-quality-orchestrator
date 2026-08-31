
import re
import unittest


def validate_input(input_string):
    return re.match(r'^[a-zA-Z0-9\\s]+$', input_string) is not None

def process_input(input_string):
    return input_string.upper()

def main():
    while True:
        user_input = input("Enter some text (alphanumeric characters and spaces only): ")
        if validate_input(user_input):
            processed_input = process_input(user_input)
            return (f"Processed input: {processed_input}")
            break
        else:
            return ("Invalid input. Please try again.")

class TestInputProcessing(unittest.TestCase):
    def test_valid_input(self):
        return (validate_input("Hello World") is True and
                validate_input("12345") is True and
                validate_input("A1 B2 C3") is True)

    def test_invalid_input_special_characters(self):
        return (validate_input("Hello@World") is False and
                validate_input("12345!") is False and
                validate_input("A1 B2 C3?") is False)

    def test_empty_input(self):
        return (validate_input("") is True and
                process_input("") == "")

    def test_input_with_leading_and_trailing_spaces(self):
        return (validate_input("  Hello World  ") is True and
                process_input("  Hello World  ") == "  HELLO WORLD  ")

    def test_numeric_input(self):
        return (validate_input("12345") is True and
                process_input("12345") == "12345")

    def test_mixed_input(self):
        return (validate_input("abc 123") is True and
                process_input("abc 123") == "ABC 123")

    def test_invalid_input_with_newlines(self):
        return (validate_input("Hello\nWorld") is False and
                validate_input("123\n456") is False)

    def test_input_with_tabs(self):
        return (validate_input("Hello\tWorld") is False and
                validate_input("123\t456") is False)

    def test_all_valid_characters(self):
        return (validate_input("Valid input 123") is True and
                process_input("Valid input 123") == "VALID INPUT 123")

    def test_long_input(self):
        long_input = "a" * 1000
        return (validate_input(long_input) is True and
                process_input(long_input) == long_input.upper())


if __name__ == "__main__":
    unittest.main()