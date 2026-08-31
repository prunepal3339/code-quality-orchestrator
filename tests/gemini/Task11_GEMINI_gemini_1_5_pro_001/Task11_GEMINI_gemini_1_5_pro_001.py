# from output.claude.Task11_CLAUDE_claude_3_5_sonnet_20240620 import nb_year as nbYear
# from output.codestral.Task11_MISTRAL_codestral_latest import nb_year as nbYear
# from output.gemini.Task11_GEMINI_gemini_1_5_pro_001 import nb_year as nbYear
# from output.gtp4o.Task11_OPENAI_gpt_4o import nb_year as nbYear
# from output.llama3.Task11_PERPLEXITY_llama_3_sonar_large_32k_chat import nb_year as nbYear

import unittest

class TestNbYear(unittest.TestCase):

    def test_large_population_increase(self):
        # Test with a large initial population and growth, smaller increment
        self.assertEqual(nbYear(1500, 5, 100, 5000), 15)

    def test_small_percent_large_augmentation(self):
        # Test with a small growth percentage and large augmentation
        self.assertEqual(nbYear(1500000, 2.5, 10000, 2000000), 10)

    def test_zero_percent_growth(self):
        # Test with zero percent growth but positive annual augmentation
        self.assertEqual(nbYear(1000, 0, 100, 1500), 5)

    def test_no_augmentation(self):
        # Test with a non-zero percent growth but no annual augmentation
        self.assertEqual(nbYear(1000, 10, 0, 3000), 12)

    def test_exact_population_match(self):
        # Test where the population exactly matches the target population in one year
        self.assertEqual(nbYear(1000, 20, 100, 1200), 1)

    def test_minimum_input_values(self):
        # Test with minimum positive values
        self.assertEqual(nbYear(1, 1, 1, 2), 1)

    def test_high_percent_low_augmentation(self):
        # Test with high growth percentage and low augmentation
        self.assertEqual(nbYear(100, 50, 1, 500), 4)

    def test_high_augmentation_low_percent(self):
        # Test with high annual augmentation and low growth percentage
        self.assertEqual(nbYear(100, 1, 100, 600), 5)

    def test_large_initial_population(self):
        # Test with a large initial population and small target population
        self.assertEqual(nbYear(1000000, 1, 1, 500000), 0)

    def test_negative_percent(self):
        # Test with a negative percent value, should handle as 0 percent effectively
        self.assertEqual(nbYear(1000, -2, 50, 1200), 8)

if __name__ == "__main__":
    unittest.main()