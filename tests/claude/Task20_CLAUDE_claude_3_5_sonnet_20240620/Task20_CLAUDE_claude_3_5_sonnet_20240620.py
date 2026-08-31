from output.claude.Task20_CLAUDE_claude_3_5_sonnet_20240620 import dig_pow as dig_pow
# from output.codestral.Task20_MISTRAL_codestral_latest import dig_pow as dig_pow
# from output.gemini.Task20_GEMINI_gemini_1_5_pro_001 import dig_pow as dig_pow
# from output.gtp4o.Task20_OPENAI_gpt_4o import dig_pow as dig_pow
# from output.llama3.Task20_PERPLEXITY_llama_3_sonar_large_32k_chat import dig_pow as dig_pow
import unittest


class TestDigPow(unittest.TestCase):

    def test_basic_example_1(self):
        # Test with example where n = 89 and p = 1
        self.assertEqual(dig_pow(89, 1), 1)

    def test_basic_example_2(self):
        # Test with example where n = 92 and p = 1
        self.assertEqual(dig_pow(92, 1), -1)

    def test_basic_example_3(self):
        # Test with example where n = 695 and p = 2
        self.assertEqual(dig_pow(695, 2), 2)

    def test_no_solution(self):
        # Test where no k exists for the given n and p
        self.assertEqual(dig_pow(123, 2), -1)

    def test_single_digit(self):
        # Test with a single digit number n = 5 and p = 1
        self.assertEqual(dig_pow(5, 1), 1)

    def test_consecutive_powers(self):
        # Test with consecutive powers where n = 135 and p = 1
        self.assertEqual(dig_pow(135, 1), 1)

    def test_larger_value(self):
        # Test with larger values where n = 1000 and p = 2
        self.assertEqual(dig_pow(1000, 2), -1)

    def test_another_example(self):
        # Test with another example where n = 135 and p = 2
        self.assertEqual(dig_pow(135, 2), -1) #todo : fix in java

    def test_all_digits_same(self):
        # Test where all digits are the same n = 111 and p = 1
        self.assertEqual(dig_pow(111, 1), -1)

    def test_leading_zeros(self):
        # Test where input includes leading zeros, although not typical, should handle gracefully
        self.assertEqual(dig_pow(100, 1), -1)

if __name__ == '__main__':
    unittest.main()