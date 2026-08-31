# from output.claude.Task30_CLAUDE_claude_3_5_sonnet_20240620 import longest as longest
# from output.codestral.Task30_MISTRAL_codestral_latest import longest as longest
# from output.gemini.Task30_GEMINI_gemini_1_5_pro_001 import longest as longest
# from output.gtp4o.Task30_OPENAI_gpt_4o import longest as longest
# from output.llama3.Task30_PERPLEXITY_llama_3_sonar_large_32k_chat import longest as longest
import unittest
class TestLongest(unittest.TestCase):

    def test_distinct_characters(self):
        # Test with distinct characters in s1 and s2
        self.assertEqual(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"), "abcdefklmopqwxy")

    def test_identical_strings(self):
        # Test with identical strings
        self.assertEqual(longest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"), "abcdefghijklmnopqrstuvwxyz")

    def test_empty_strings(self):
        # Test with both strings empty
        self.assertEqual(longest("", ""), "")

    def test_one_empty_string(self):
        # Test with one string empty and the other full
        self.assertEqual(longest("", "abcdef"), "abcdef")

    def test_no_overlapping_characters(self):
        # Test with no overlapping characters between s1 and s2
        self.assertEqual(longest("abc", "def"), "abcdef")

    def test_all_overlapping_characters(self):
        # Test with all characters in s1 and s2 overlapping
        self.assertEqual(longest("abc", "abcd"), "abcd")

    def test_case_insensitive(self):
        # Test with case sensitivity (input should only include lowercase letters)
        self.assertEqual(longest("abc", "xyzf"), "abcfxyz")

    def test_long_strings(self):
        # Test with long strings
        s1 = "abcdefghijklmnopqrstuvwxyzaaa"
        s2 = "zyxwvutsrqponmlkjihgfedcbaaaa"
        self.assertEqual(longest(s1, s2), "abcdefghijklmnopqrstuvwxyz")

    def test_single_character_strings(self):
        # Test with single character strings
        self.assertEqual(longest("a", "a"), "a")

    def test_repeated_characters(self):
        # Test with repeated characters in both strings
        self.assertEqual(longest("aaaa", "bbbbccccdddd"), "abcd")

if __name__ == '__main__':
    unittest.main()