# from output.claude.Task29_CLAUDE_claude_3_5_sonnet_20240620 import two_sum as two_sum
from output.codestral.Task29_MISTRAL_codestral_latest import two_sum as two_sum
# from output.gemini.Task29_GEMINI_gemini_1_5_pro_001 import two_sum as two_sum
# from output.gtp4o.Task29_OPENAI_gpt_4o import two_sum as two_sum
# from output.llama3.Task29_PERPLEXITY_llama_3_sonar_large_32k_chat import two_sum as two_sum
import unittest

class TestTwoSum(unittest.TestCase):


    def test_case_1(self):
        numbers = [1, 2, 3]
        target = 4
        expected = [0, 2]  # 1 + 3 = 4
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case_2(self):
        numbers = [3, 2, 4]
        target = 6
        expected = [1, 2]  # 2 + 4 = 6
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case_3(self):
        numbers = [1, -2, 3, 4]
        target = 7
        expected = [2, 3]  # 3 + 4 = 7
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case_4(self):
        numbers = [0, 1, 2]
        target = 3
        expected = [1, 2]  # 1 + 2 = 3
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case_5(self):
        numbers = [2, 2, 3]
        target = 4
        expected = [0, 1]  # 2 + 2 = 4
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case_6(self):
        numbers = [5, 7, 3, 9]
        target = 12
        expected = [0, 1]  # 7 + 5 = 12
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case_7(self):
        numbers = [-5, -2, -3, 1]
        target = -7
        expected = [0, 1]  # -5 + (-2) = -7
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case_8(self):
        numbers = [10, 20, 30, 40]
        target = 50
        expected = [0, 3]  # 10 + 40 = 50
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case_9(self):
        numbers = [1, 2, 5, 9]
        target = 14
        expected = [2, 3]  # 5 + 9 = 14
        self.assertEqual(two_sum(numbers, target), expected)

    def test_case_10(self):
        numbers = [7, 14, 21, 28]
        target = 35
        expected = [0, 3]  # 7 + 28 = 35
        # self.assertEqual(two_sum(numbers, target), expected)
        self.assertEqual(two_sum(numbers, target), expected)

if __name__ == '__main__':
    unittest.main()