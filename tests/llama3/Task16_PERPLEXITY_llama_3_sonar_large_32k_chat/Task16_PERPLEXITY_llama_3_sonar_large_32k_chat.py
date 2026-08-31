# from output.claude.Task16_CLAUDE_claude_3_5_sonnet_20240620 import solution as solution
# from output.codestral.Task16_MISTRAL_codestral_latest import solution as solution
# from output.gemini.Task16_GEMINI_gemini_1_5_pro_001 import solution as solution
# from output.gtp4o.Task16_OPENAI_gpt_4o import solution as solution
# from output.llama3.Task16_PERPLEXITY_llama_3_sonar_large_32k_chat import solution as solution
import unittest

class TestStringEnding(unittest.TestCase):

    def test_basic_true(self):
        # Test where the main string ends with the ending string
        self.assertTrue(solution("abc", "bc"))

    def test_basic_false(self):
        # Test where the main string does not end with the ending string
        self.assertFalse(solution("abc", "d"))

    def test_empty_ending(self):
        # Test where the ending string is empty
        self.assertTrue(solution("abc", ""))

    def test_empty_string(self):
        # Test where the main string is empty
        self.assertFalse(solution("", "a"))

    def test_ending_is_main_string(self):
        # Test where the ending string is the same as the main string
        self.assertTrue(solution("hello", "hello"))

    def test_ending_longer_than_main_string(self):
        # Test where the ending string is longer than the main string
        self.assertFalse(solution("short", "longerEnding"))

    def test_ending_at_start(self):
        # Test where the ending string appears at the start of the main string
        self.assertFalse(solution("startmiddleend", "start"))

    def test_ending_is_substring(self):
        # Test where the ending string is a substring but not at the end
        self.assertFalse(solution("substring", "str"))

    def test_case_sensitive_ending(self):
        # Test case sensitivity by checking a lowercase ending in an uppercase string
        self.assertFalse(solution("HELLO", "hello"))

    def test_multiple_occurrences(self):
        # Test with multiple occurrences of the ending string in the main string
        self.assertTrue(solution("testtesttest", "test"))

if __name__ == "__main__":
    unittest.main()