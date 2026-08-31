# from output.claude.Task10_CLAUDE_claude_3_5_sonnet_20240620 import get_sum as getSum
# from output.codestral.Task10_MISTRAL_codestral_latest import get_sum as getSum
# from output.gemini.Task10_GEMINI_gemini_1_5_pro_001 import get_sum as getSum
# from output.gtp4o.Task10_OPENAI_gpt_4o import get_sum as getSum
# from output.llama3.Task10_PERPLEXITY_llama_3_sonar_large_32k_chat import sum_between as getSum
import unittest

class TestGetSum(unittest.TestCase):

    def test_positive_range(self):
        # Test with positive numbers where a < b
        self.assertEqual(getSum(1, 2), 3)

    def test_positive_range_reversed(self):
        # Test with positive numbers where b < a
        self.assertEqual(getSum(2, 1), 3)

    def test_single_number(self):
        # Test with a single number
        self.assertEqual(getSum(5, 5), 5)

    def test_zero_in_range(self):
        # Test with a range that includes zero
        self.assertEqual(getSum(0, 1), 1)

    def test_negative_to_positive(self):
        # Test with a range from negative to positive numbers
        self.assertEqual(getSum(-1, 2), 2)

    def test_negative_range(self):
        # Test with negative numbers where a < b
        self.assertEqual(getSum(-3, -1), -6)

    def test_negative_range_reversed(self):
        # Test with negative numbers where b < a
        self.assertEqual(getSum(-1, -3), -6)

    def test_positive_and_negative_range(self):
        # Test with a mix of positive and negative numbers where a < b
        self.assertEqual(getSum(-2, 1), -2)

    def test_positive_and_negative_range_reversed(self):
        # Test with a mix of positive and negative numbers where b < a
        self.assertEqual(getSum(1, -2), -2)
    def test_large_range(self):
        # Test with a large range from -100 to 100
        self.assertEqual(getSum(-100, 100), 0)

if __name__ == "__main__":
    unittest.main()
