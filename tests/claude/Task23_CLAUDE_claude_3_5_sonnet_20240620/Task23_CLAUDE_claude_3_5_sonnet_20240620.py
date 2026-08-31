# from output.claude.Task23_CLAUDE_claude_3_5_sonnet_20240620 import find_nb as find_nb
# from output.codestral.Task23_MISTRAL_codestral_latest import find_nb as find_nb
# from output.gemini.Task23_GEMINI_gemini_1_5_pro_001 import find_nb as find_nb
# from output.gtp4o.Task23_OPENAI_gpt_4o import findNb as find_nb
from output.llama3.Task23_PERPLEXITY_llama_3_sonar_large_32k_chat import find_nb as find_nb
import unittest


class TestFindNb(unittest.TestCase):

    def test_case1(self):
        m = 1071225
        expected = 45
        self.assertEqual(find_nb(m), expected)

    def test_case2(self):
        m = 91716553919377
        expected = -1
        self.assertEqual(find_nb(m), expected)

    def test_case3(self):
        m = 1
        expected = 1
        self.assertEqual(find_nb(m), expected)

    def test_case4(self):
        m = 9
        expected = 2
        self.assertEqual(find_nb(m), expected)

    def test_case5(self):
        m = 36
        expected = 3
        self.assertEqual(find_nb(m), expected)

    def test_case6(self):
        m = 1000
        expected = 10
        self.assertEqual(find_nb(m), expected)

    def test_case7(self):
        m = 2025
        expected = -1
        self.assertEqual(find_nb(m), expected)

    def test_case8(self):
        m = 1000000
        expected = 20
        self.assertEqual(find_nb(m), expected)

    def test_case9(self):
        m = 2552550
        expected = -1
        self.assertEqual(find_nb(m), expected)

    def test_case10(self):
        m = 3375
        expected = 6
        self.assertEqual(find_nb(m), expected)

if __name__ == '__main__':
    unittest.main()