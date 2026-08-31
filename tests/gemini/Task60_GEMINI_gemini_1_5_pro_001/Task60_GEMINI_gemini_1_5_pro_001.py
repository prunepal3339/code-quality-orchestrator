

# from output.claude.Task60_CLAUDE_claude_3_5_sonnet_20240620 import expanded_form as expanded_form
# from output.codestral.Task60_MISTRAL_codestral_latest import expanded_form as expanded_form
# from output.gemini.Task60_GEMINI_gemini_1_5_pro_001 import expanded_form as expanded_form
# from output.gtp4o.Task60_OPENAI_gpt_4o import expanded_form as expanded_form
# from output.llama3.Task60_PERPLEXITY_llama_3_sonar_large_32k_chat import expanded_form as expanded_form
import unittest

class TestExpandedFormFunction(unittest.TestCase):

    def test_two_digit_number(self):
        self.assertEqual(expanded_form(12), "10 + 2")

    def test_two_digit_number_with_zero(self):
        self.assertEqual(expanded_form(42), "40 + 2")

    def test_five_digit_number(self):
        self.assertEqual(expanded_form(70304), "70000 + 300 + 4")

    def test_single_digit_number(self):
        self.assertEqual(expanded_form(5), "5")

    def test_number_with_zeros(self):
        self.assertEqual(expanded_form(1001), "1000 + 1")

    def test_large_number(self):
        self.assertEqual(expanded_form(123456), "100000 + 20000 + 3000 + 400 + 50 + 6")

    def test_number_with_repeated_digits(self):
        self.assertEqual(expanded_form(2222), "2000 + 200 + 20 + 2")

    def test_number_with_only_zeros_after_first_digit(self):
        self.assertEqual(expanded_form(50000), "50000")

    def test_number_with_only_zeros_before_last_digit(self):
        self.assertEqual(expanded_form(10005), "10000 + 5")

    def test_edge_case_smallest_number(self):
        self.assertEqual(expanded_form(1), "1")

if __name__ == '__main__':
    unittest.main()