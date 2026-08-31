from output.claude.Task6_CLAUDE_claude_3_5_sonnet_20240620 import find_uniq as findUniq
# from output.codestral.Task8_MISTRAL_codestral_latest import find_missing_letter as find_missing_letter
# from output.gemini.Task6_GEMINI_gemini_1_5_pro_001 import find_uniq as findUniq
# from output.gtp4o.Task6_OPENAI_gpt_4o import find_uniq as findUniq
# from output.llama3.Task6_PERPLEXITY_llama_3_sonar_large_32k_chat import find_uniq as findUniq
import unittest



class TestFindUniq(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(findUniq([1, 1, 1, 2, 1, 1]), 2.0)

    def test_case_2(self):
        self.assertEqual(findUniq([0, 0, 0.55, 0, 0]), 0.55)

    def test_case_3(self):
        self.assertEqual(findUniq([3, 2, 2, 2, 2]), 3.0)

    def test_case_4(self):
        self.assertEqual(findUniq([1, 1, 5.5, 1, 1]), 5.5)

    def test_case_5(self):
        self.assertEqual(findUniq([-1, -1, -1, -3.5, -1]), -3.5)

    def test_case_6(self):
        self.assertEqual(findUniq([100.1, 100, 100, 100, 100]), 100.1)

    def test_case_7(self):
        self.assertEqual(findUniq([0, 0, -2, 0, 0]), -2.0)

    def test_case_8(self):
        self.assertEqual(findUniq([0.1, 0.1, 0.123, 0.1, 0.1]), 0.123)

    def test_case_9(self):
        with self.assertRaises(Exception):
            findUniq([10, 10, 7, 9.999, 10])

    def test_case_10(self):
        self.assertEqual(findUniq([-7, -7, -7.7, -7, -7]), -7.7)


if __name__ == '__main__':
    unittest.main()
