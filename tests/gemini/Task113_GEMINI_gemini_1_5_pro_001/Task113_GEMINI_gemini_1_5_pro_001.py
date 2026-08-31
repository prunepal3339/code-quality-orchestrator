import unittest


def foo(num_strings,user_string):
    concatenated_string = ""
    for i in range(num_strings):
        concatenated_string += user_string
    return concatenated_string


class TestFooFunction(unittest.TestCase):


    def test_single_string(self):
        # Test with a single string, repeat once
        result = foo(1, "Hello")
        # It should return the string itself since it's repeated once
        self.assertEqual(result, "Hello")

    def test_empty_string(self):
        # Test with an empty string
        result = foo(1, "")
        # Since the string is empty, even with one repetition, the result should be empty
        self.assertEqual(result, "")

    def test_multiple_repetitions(self):
        # Test with a string repeated multiple times
        result = foo(3, "abc")
        # The string "abc" should be repeated 3 times
        self.assertEqual(result, "abcabcabc")

    def test_no_repetitions(self):
        # Test with zero repetitions
        result = foo(0, "Hello")
        # No matter what the string is, with 0 repetitions, the result should be empty
        self.assertEqual(result, "")

    def test_large_repetition(self):
        # Test with a large number of repetitions
        result = foo(1000, "a")
        # The string "a" should be repeated 1000 times
        self.assertEqual(result, "a" * 1000)

if __name__ == '__main__':
    unittest.main()
