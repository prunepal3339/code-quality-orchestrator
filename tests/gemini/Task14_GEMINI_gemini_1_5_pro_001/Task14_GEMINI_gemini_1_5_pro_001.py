# from output.claude.Task14_CLAUDE_claude_3_5_sonnet_20240620 import find_even_index as find_even_index
# from output.codestral.Task14_MISTRAL_codestral_latest import find_even_index as find_even_index
# from output.gemini.Task14_GEMINI_gemini_1_5_pro_001 import find_even_index as find_even_index
# from output.gtp4o.Task14_OPENAI_gpt_4o import find_even_index as find_even_index
# from output.llama3.Task14_PERPLEXITY_llama_3_sonar_large_32k_chat import find_even_index as find_even_index
import unittest



class TestFindEvenIndex(unittest.TestCase):

    def test_case1(self):
        arr = [1, 2, 3, 4, 3, 2, 1]
        expected = 3
        self.assertEqual(find_even_index(arr), expected)

    def test_case2(self):
        arr = [1, 100, 50, -51, 1, 1]
        expected = 1
        self.assertEqual(find_even_index(arr), expected)

    def test_case3(self):
        arr = [20, 10, -80, 10, 10, 15, 35]
        expected = 0
        self.assertEqual(find_even_index(arr), expected)

    def test_case4(self):
        arr = [1, 2, 3, 4, 5, 6]
        expected = -1
        self.assertEqual(find_even_index(arr), expected)

    def test_case5(self):
        arr = [10, -10, 5, 5, 5]
        expected = 3
        self.assertEqual(find_even_index(arr), expected)

    def test_case6(self):
        arr = [-1, -2, -3, -4, -3, -2, -1]
        expected = 3
        self.assertEqual(find_even_index(arr), expected)

    def test_case7(self):
        arr = [0, 0, 0, 0, 0]
        expected = 0
        self.assertEqual(find_even_index(arr), expected)

    def test_case8(self):
        arr = [10, 20, 30, 40, 50, 60]
        expected = -1
        self.assertEqual(find_even_index(arr), expected)

    def test_case9(self):
        arr = [1, 1, 1, 1, 1, 1, 1, 6]
        expected = 6
        self.assertEqual(find_even_index(arr), expected)

    def test_case10(self):
        arr = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]
        expected = 3
        self.assertEqual(find_even_index(arr), expected)

if __name__ == "__main__":
    unittest.main()