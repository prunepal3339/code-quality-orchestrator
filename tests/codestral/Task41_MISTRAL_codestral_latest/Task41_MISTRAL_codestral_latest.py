import unittest
from unittest.mock import patch

# from output.claude.Task41_CLAUDE_claude_3_5_sonnet_20240620 import process_input as process_input
# from output.codestral.Task41_MISTRAL_codestral_latest import process_string as process_input
# from output.llama3.Task41_PERPLEXITY_llama_3_sonar_large_32k_chat import process_string as process_input

class TestProcessInput(unittest.TestCase):

    # Test for normal input within 100 characters
    def test_normal_input(self):
        self.assertEqual(process_input("Hello, world!"), "Processed input: Hello, world!")

    # Test for input exactly 100 characters long
    def test_input_100_chars(self):
        input_str = "a" * 100
        self.assertEqual(process_input(input_str), f"Processed input: {input_str}")

    # Test for input longer than 100 characters
    def test_input_longer_than_100_chars(self):
        input_str = "a" * 150
        self.assertEqual(process_input(input_str[:100]), f"Processed input: {input_str[:100]}")

    # Test for empty input
    def test_empty_input(self):
        self.assertEqual(process_input(""), "Processed input: ")

    # Test for input with special characters
    def test_input_special_chars(self):
        self.assertEqual(process_input("@#$%^&*()"), "Processed input: @#$%^&*()")

    # Test for numeric input
    def test_numeric_input(self):
        self.assertEqual(process_input("1234567890"), "Processed input: 1234567890")

    # Test for mixed alphanumeric input
    def test_mixed_input(self):
        self.assertEqual(process_input("Hello123"), "Processed input: Hello123")

    # Test for whitespace input
    def test_whitespace_input(self):
        self.assertEqual(process_input("     "), "Processed input:      ")

    # Test for input with newline characters
    def test_newline_input(self):
        self.assertEqual(process_input("Hello\nWorld"), "Processed input: Hello\nWorld")

    # Test for input with leading/trailing spaces
    def test_leading_trailing_spaces(self):
        self.assertEqual(process_input("  Hello  "), "Processed input:   Hello  ")

if __name__ == "__main__":
    unittest.main()