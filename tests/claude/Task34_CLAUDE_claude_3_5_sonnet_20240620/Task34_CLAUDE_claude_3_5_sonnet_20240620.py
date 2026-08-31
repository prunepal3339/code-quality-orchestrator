# from output.claude.Task34_CLAUDE_claude_3_5_sonnet_20240620 import narcissistic as narcissistic
# from output.codestral.Task34_MISTRAL_codestral_latest import narcissistic as narcissistic
# from output.gemini.Task34_GEMINI_gemini_1_5_pro_001 import narcissistic as narcissistic
# from output.gtp4o.Task34_OPENAI_gpt_4o import is_narcissistic as narcissistic
# from output.llama3.Task34_PERPLEXITY_llama_3_sonar_large_32k_chat import narcissistic as narcissistic
import unittest
class TestTask34(unittest.TestCase):

    def test_three_digit_narcissistic(self):
        # 153 is a known 3-digit Narcissistic number
        self.assertTrue(narcissistic(153))

    def test_three_digit_non_narcissistic(self):
        # 123 is not a Narcissistic number
        self.assertFalse(narcissistic(123))

    def test_four_digit_narcissistic(self):
        # 1634 is a known 4-digit Narcissistic number
        self.assertTrue(narcissistic(1634))

    def test_four_digit_non_narcissistic(self):
        # 1652 is not a Narcissistic number
        self.assertFalse(narcissistic(1652))

    def test_single_digit_narcissistic(self):
        # All single-digit numbers are Narcissistic
        self.assertTrue(narcissistic(5))

    def test_large_narcissistic_number(self):
        # 9474 is a known 4-digit Narcissistic number
        self.assertTrue(narcissistic(9474))

    def test_large_non_narcissistic_number(self):
        # 9475 is not a Narcissistic number
        self.assertFalse(narcissistic(9475))

    def test_five_digit_narcissistic(self):
        # 54748 is a known 5-digit Narcissistic number
        self.assertTrue(narcissistic(54748))

    def test_five_digit_non_narcissistic(self):
        # 12345 is not a Narcissistic number
        self.assertFalse(narcissistic(12345))

    def test_edge_case_single_digit_one(self):
        # 1 is a Narcissistic number
        self.assertTrue(narcissistic(1))

if __name__ == '__main__':
    unittest.main()