# from output.claude.Task8_CLAUDE_claude_3_5_sonnet_20240620 import find_missing_letter as find_missing_letter
# from output.codestral.Task8_MISTRAL_codestral_latest import find_missing_letter as find_missing_letter
# from output.gemini.Task8_GEMINI_gemini_1_5_pro_001 import find_missing_letter as find_missing_letter
from output.gtp4o.Task8_OPENAI_gpt_4o import find_missing_letter as find_missing_letter
# from output.llama3.Task8_PERPLEXITY_llama_3_sonar_large_32k_chat import find_missing_letter as find_missing_letter
import unittest


import unittest

class TestFindMissingLetter(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')

    def test_case_2(self):
        self.assertEqual(find_missing_letter(['b', 'c', 'd', 'f', 'g']), 'e')

    def test_case_3(self):
        self.assertEqual(find_missing_letter(['a', 'c', 'd', 'e', 'f', 'g']), 'b')

    def test_case_4(self):
        self.assertEqual(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')

    def test_case_5(self):
        self.assertEqual(find_missing_letter(['C', 'D', 'E', 'G', 'H']), 'F')

    def test_case_6(self):
        self.assertEqual(find_missing_letter(['A', 'B', 'D', 'E', 'F', 'G']), 'C')

    def test_case_7(self):
        self.assertEqual(find_missing_letter(['a', 'b', 'd']), 'c')

    def test_case_8(self):
        self.assertEqual(find_missing_letter(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n']), 'm')

    def test_case_9(self):
        self.assertEqual(find_missing_letter(['X', 'Z']), 'Y')

    def test_case_10(self):
        self.assertEqual(find_missing_letter(['a', 'c']), 'b')

if __name__ == '__main__':
    unittest.main()

