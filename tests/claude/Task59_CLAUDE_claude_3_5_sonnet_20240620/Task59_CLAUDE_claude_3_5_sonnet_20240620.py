import unittest

# from output.claude.Task59_CLAUDE_claude_3_5_sonnet_20240620 import accum as accum
# from output.codestral.Task59_MISTRAL_codestral_latest import accum as accum
# from output.gemini.Task59_GEMINI_gemini_1_5_pro_001 import accum
# from output.gtp4o.Task59_OPENAI_gpt_4o import accum
# from output.llama3.Task59_PERPLEXITY_llama_3_sonar_large_32k_chat import accum

class TestAccumFunction(unittest.TestCase):

    def test_all_unique_characters(self):
        self.assertEqual(accum("abcd"), "A-Bb-Ccc-Dddd")

    def test_mixed_case_characters(self):
        self.assertEqual(accum("RqaEzty"), "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy")

    def test_mixed_case_characters_with_repeating(self):
        self.assertEqual(accum("cwAt"), "C-Ww-Aaa-Tttt")

    def test_single_character_string(self):
        self.assertEqual(accum("a"), "A")

    def test_all_uppercase_characters(self):
        self.assertEqual(accum("XYZ"), "X-Yy-Zzz")

    def test_all_lowercase_characters(self):
        self.assertEqual(accum("xyz"), "X-Yy-Zzz")

    def test_mixed_case_with_repeating_characters(self):
        self.assertEqual(accum("aAaA"), "A-Aa-Aaa-Aaaa")

    def test_empty_string(self):
        self.assertEqual(accum(""), "")

    def test_string_with_repeated_characters(self):
        self.assertEqual(accum("aaabbb"), "A-Aa-Aaa-Bbbb-Bbbbb-Bbbbbb")

    def test_case_sensitivity_check(self):
        self.assertEqual(accum("AaBbCc"), "A-Aa-Bbb-Bbbb-Ccccc-Cccccc")

if __name__ == '__main__':
    unittest.main()