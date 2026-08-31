# from output.claude.Task17_CLAUDE_claude_3_5_sonnet_20240620 import to_jaden_case as to_jaden_case
# from output.codestral.Task17_MISTRAL_codestral_latest import to_jaden_case as to_jaden_case
# from output.gemini.Task17_GEMINI_gemini_1_5_pro_001 import to_jaden_case as to_jaden_case
# from output.gtp4o.Task17_OPENAI_gpt_4o import to_jaden_case as to_jaden_case
from output.llama3.Task17_PERPLEXITY_llama_3_sonar_large_32k_chat import to_jaden_case as to_jaden_case
import unittest

class TestJadenCase(unittest.TestCase):

    def test_basic_case1(self):
        # Test standard phrase conversion to Jaden Case
        phrase = "how can mirrors be real if our eyes aren't real"
        expected = "How Can Mirrors Be Real If Our Eyes Aren't Real"
        self.assertEqual(to_jaden_case(phrase), expected)

    def test_basic_case2(self):
        # Test another standard phrase conversion to Jaden Case
        phrase = "the karate kid is a great movie"
        expected = "The Karate Kid Is A Great Movie"
        self.assertEqual(to_jaden_case(phrase), expected)

    def test_basic_case3(self):
        # Test phrase with numbers
        phrase = "after earth was released in 2013"
        expected = "After Earth Was Released In 2013"
        self.assertEqual(to_jaden_case(phrase), expected)

    def test_basic_case4(self):
        # Test phrase with common sentence structure
        phrase = "i think therefore i am"
        expected = "I Think Therefore I Am"
        self.assertEqual(to_jaden_case(phrase), expected)

    def test_basic_case5(self):
        # Test phrase with repeated words
        phrase = "to be or not to be"
        expected = "To Be Or Not To Be"
        self.assertEqual(to_jaden_case(phrase), expected)

    def test_basic_case6(self):
        # Test phrase with simple words
        phrase = "life is but a dream"
        expected = "Life Is But A Dream"
        self.assertEqual(to_jaden_case(phrase), expected)

    def test_basic_case7(self):
        # Test phrase with punctuation
        phrase = "it's a beautiful day in the neighborhood"
        expected = "It's A Beautiful Day In The Neighborhood"
        self.assertEqual(to_jaden_case(phrase), expected)

    def test_edge_case_empty_string(self):
        # Test empty string
        phrase = ""
        self.assertEqual(to_jaden_case(phrase), "")

    def test_edge_case_none(self):
        # Test None input
        phrase = None
        self.assertIsNone(to_jaden_case(phrase))

    def test_edge_case_mixed_case(self):
        # Test phrase with mixed case words
        phrase = "a qUICK bROWN fOX jUMPS oVER tHE lAZY dOG"
        expected = "A Quick Brown Fox Jumps Over The Lazy Dog"
        self.assertEqual(to_jaden_case(phrase), expected)

if __name__ == "__main__":
    unittest.main()