
import unittest

# from output.claude.Task58_CLAUDE_claude_3_5_sonnet_20240620 import XO as xo
# from output.codestral.Task58_MISTRAL_codestral_latest import XO as xo
# from output.gemini.Task58_GEMINI_gemini_1_5_pro_001 import XO as xo
# from output.gtp4o.Task58_OPENAI_gpt_4o import XO as xo
# from output.llama3.Task58_PERPLEXITY_llama_3_sonar_large_32k_chat import xo
class TestXOFunction(unittest.TestCase):

    def test_all_x_and_o(self):
        self.assertTrue(xo("ooxx"))

    def test_more_x_than_o(self):
        self.assertFalse(xo("xooxx"))

    def test_more_o_than_x(self):
        self.assertTrue(xo("xxoo"))

    def test_case_insensitive(self):
        self.assertTrue(xo("ooxXm"))

    def test_no_x_no_o(self):
        self.assertTrue(xo("zpzpzpp"))

    def test_no_x_with_o(self):
        self.assertFalse(xo("zzoo"))

    def test_no_o_with_x(self):
        self.assertFalse(xo("xxxx"))

    def test_empty_string(self):
        self.assertTrue(xo(""))

    def test_single_character_o(self):
        self.assertFalse(xo("o"))

    def test_single_character_x(self):
        self.assertFalse(xo("x"))

if __name__ == '__main__':
    unittest.main()
