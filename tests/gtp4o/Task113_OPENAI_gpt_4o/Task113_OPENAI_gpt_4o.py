def foo(input_str1,input_str2):
    result = input_str1 + input_str2
    return result

import unittest

class TestFooFunction(unittest.TestCase):

    def test_concatenate_two_strings(self):
        # Test with two non-empty strings
        result = foo("Hello", "World")
        # The result should be the concatenation of "Hello" and "World"
        self.assertEqual(result, "HelloWorld")

    def test_concatenate_with_empty_string(self):
        # Test with the first string empty and the second string non-empty
        result = foo("", "World")
        # The result should be just "World"
        self.assertEqual(result, "World")

        # Test with the first string non-empty and the second string empty
        result = foo("Hello", "")
        # The result should be just "Hello"
        self.assertEqual(result, "Hello")

        # Test with both strings empty
        result = foo("", "")
        # The result should be an empty string
        self.assertEqual(result, "")

    def test_concatenate_special_characters(self):
        # Test with special characters
        result = foo("!@#", "$%^")
        # The result should be "!@#$%^"
        self.assertEqual(result, "!@#$%^")

    def test_concatenate_with_spaces(self):
        # Test with strings containing spaces
        result = foo("Hello ", "World")
        # The result should be "Hello World" (with a space between)
        self.assertEqual(result, "Hello World")

if __name__ == '__main__':
    unittest.main()