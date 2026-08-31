# from output.claude.Task27_CLAUDE_claude_3_5_sonnet_20240620 import find_outlier as find_outlier
# from output.codestral.Task27_MISTRAL_codestral_latest import find_outlier as find_outlier
# from output.gemini.Task27_GEMINI_gemini_1_5_pro_001 import find_outlier as find_outlier
# from output.gtp4o.Task27_OPENAI_gpt_4o import find_outlier as find_outlier
# from output.llama3.Task27_PERPLEXITY_llama_3_sonar_large_32k_chat import find_outlier as find_outlier
import unittest

class TestTask27(unittest.TestCase):

    def test_case1(self):
        input_data = [2, 4, 0, 100, 4, 11, 2602, 36]
        expected = 11
        self.assertEqual(find_outlier(input_data), expected)

    def test_case2(self):
        input_data = [160, 3, 1719, 19, 11, 13, -21]
        expected = 160
        self.assertEqual(find_outlier(input_data), expected)

    def test_case3(self):
        input_data = [1, 3, 5, 7, 8]
        expected = 8
        self.assertEqual(find_outlier(input_data), expected)

    def test_case4(self):
        input_data = [2, 4, 6, 8, 10, 13]
        expected = 13
        self.assertEqual(find_outlier(input_data), expected)

    def test_case5(self):
        input_data = [10, 12, 14, 16, 18, 21, 22]
        expected = 21
        self.assertEqual(find_outlier(input_data), expected)

    def test_case6(self):
        input_data = [1, 2, 3]
        expected = 2
        self.assertEqual(find_outlier(input_data), expected)

    def test_case7(self):
        input_data = [3, 5, 7, 11, 2]
        expected = 2
        self.assertEqual(find_outlier(input_data), expected)

    def test_case8(self):
        input_data = [2, 2, 2, 2, 1]
        expected = 1
        self.assertEqual(find_outlier(input_data), expected)

    def test_case9(self):
        input_data = [11, 13, 15, 17, 19, 20]
        expected = 20
        self.assertEqual(find_outlier(input_data), expected)

    def test_case10(self):
        input_data = [4, 8, 12, 16, 20, 21, 24]
        expected = 21
        self.assertEqual(find_outlier(input_data), expected)

if __name__ == '__main__':
    unittest.main()