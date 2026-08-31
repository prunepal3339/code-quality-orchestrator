# from output.claude.Task22_CLAUDE_claude_3_5_sonnet_20240620 import filter_list as filter_list
# from output.codestral.Task22_MISTRAL_codestral_latest import filter_list as filter_list
# from output.gemini.Task22_GEMINI_gemini_1_5_pro_001 import filter_list as filter_list
# from output.gtp4o.Task22_OPENAI_gpt_4o import filter_list as filter_list
# from output.llama3.Task22_PERPLEXITY_llama_3_sonar_large_32k_chat import filter_list as filter_list
import unittest

class TestFilterList(unittest.TestCase):

    def test_mixed_list(self):
        # Test with a list containing integers and strings
        input_data = [1, 2, "a", "b"]
        expected = [1, 2]
        self.assertEqual(filter_list(input_data), expected)

    def test_empty_list(self):
        # Test with an empty list
        input_data = []
        expected = []
        self.assertEqual(filter_list(input_data), expected)

    def test_all_strings(self):
        # Test with a list containing only strings
        input_data = ["a", "b", "c"]
        expected = []
        self.assertEqual(filter_list(input_data), expected)

    def test_all_integers(self):
        # Test with a list containing only integers
        input_data = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        self.assertEqual(filter_list(input_data), expected)

    def test_strings_and_integers_mixed(self):
        # Test with a list of mixed strings and integers with varied content
        input_data = [1, "a", 2, "b", 0, 15]
        expected = [1, 2, 0, 15]
        self.assertEqual(filter_list(input_data), expected)

    def test_single_element_integer(self):
        # Test with a list containing a single integer
        input_data = [5]
        expected = [5]
        self.assertEqual(filter_list(input_data), expected)

    def test_single_element_string(self):
        # Test with a list containing a single string
        input_data = ["onlyString"]
        expected = []
        self.assertEqual(filter_list(input_data), expected)

    def test_integers_and_numeric_strings(self):
        # Test with a list containing integers and numeric strings
        input_data = [1, "2", "three", 4, "5"]
        expected = [1, 4]
        self.assertEqual(filter_list(input_data), expected)

    def test_negative_integers(self):
        # Test with a list containing negative integers and strings
        input_data = [-1, "-2", 3, "4"]
        expected = [-1, 3]
        self.assertEqual(filter_list(input_data), expected)

    def test_large_list(self):
        # Test with a large list of integers and strings
        input_data = [
            100, "200", 300, "400", 500, "600", 700, "800", 900, "1000",
            1100, "1200", 1300, "1400", 1500, "1600", 1700, "1800", 1900, "2000"
        ]
        expected = [
            100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900
        ]
        self.assertEqual(filter_list(input_data), expected)

if __name__ == '__main__':
    unittest.main()