# from output.claude.Task19_CLAUDE_claude_3_5_sonnet_20240620 import spin_words as spinWords
# from output.codestral.Task19_MISTRAL_codestral_latest import spin_words as spinWords
# from output.gemini.Task19_GEMINI_gemini_1_5_pro_001 import spin_words as spinWords
# from output.gtp4o.Task19_OPENAI_gpt_4o import spin_words as spinWords
# from output.llama3.Task19_PERPLEXITY_llama_3_sonar_large_32k_chat import reverse_words as spinWords
import unittest


class TestTask19(unittest.TestCase):
    def test_case1(self):
        sentence = "Hey fellow warriors"
        expected = "Hey wollef sroirraw"
        self.assertEqual(spinWords(sentence), expected)

    def test_case2(self):
        sentence = "This is a test"
        expected = "This is a test"
        self.assertEqual(spinWords(sentence), expected)

    def test_case3(self):
        sentence = "This is another test"
        expected = "This is rehtona test"
        self.assertEqual(spinWords(sentence), expected)

    def test_case4(self):
        sentence = "Welcome to the jungle"
        expected = "emocleW to the elgnuj"
        self.assertEqual(spinWords(sentence), expected)

    def test_case5(self):
        sentence = "You are amazing"
        expected = "You are gnizama"
        self.assertEqual(spinWords(sentence), expected)

    def test_case6(self):
        sentence = "Just a simple example"
        expected = "Just a elpmis elpmaxe"
        self.assertEqual(spinWords(sentence), expected)

    def test_case7(self):
        sentence = "Short words are not reversed"
        expected = "trohS sdrow are not desrever"
        self.assertEqual(spinWords(sentence), expected)

    def test_case8(self):
        sentence = "Reverse only long words"
        expected = "esreveR only long sdrow"
        self.assertEqual(spinWords(sentence), expected)

    def test_case9(self):
        sentence = "Exceptional cases should work too"
        expected = "lanoitpecxE sesac dluohs work too"
        self.assertEqual(spinWords(sentence), expected)

    def test_case10(self):
        sentence = "This sentence contains multiple long words"
        expected = "This ecnetnes sniatnoc elpitlum long sdrow"
        self.assertEqual(spinWords(sentence), expected)

if __name__ == "__main__":
    unittest.main()