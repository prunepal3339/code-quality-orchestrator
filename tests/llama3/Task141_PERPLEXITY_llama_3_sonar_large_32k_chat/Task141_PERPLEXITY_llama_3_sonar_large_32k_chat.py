import unittest


def reverse_string(s):
    return s[::-1]



class TestReverseString(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome_string(self):
        self.assertEqual(reverse_string("madam"), "madam")

    def test_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_string_with_numbers(self):
        self.assertEqual(reverse_string("12345"), "54321")

    def test_string_with_special_characters(self):
        self.assertEqual(reverse_string("!@#$%^&*()"), ")(*&^%$#@!")

    def test_string_with_mixed_case(self):
        self.assertEqual(reverse_string("HeLLo"), "oLLeH")

    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(reverse_string("  hello  "), "  olleh  ")

    def test_long_string(self):
        self.assertEqual(reverse_string("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")

if __name__ == "__main__":
    unittest.main()