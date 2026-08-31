# from output.claude.Task12_CLAUDE_claude_3_5_sonnet_20240620 import high
# from output.codestral.Task12_MISTRAL_codestral_latest import high_scoring_word as high
# from output.gemini.Task12_GEMINI_gemini_1_5_pro_001 import high
# from output.gtp4o.Task12_OPENAI_gpt_4o import high as high
# from output.llama3.Task12_PERPLEXITY_llama_3_sonar_large_32k_chat import high as high
import unittest
class TestHighFunction(unittest.TestCase):

    def test_basic_example_1(self):
        # Test basic example with diverse words
        self.assertEqual(high("man i need a taxi up to ubud"), "taxi")

    def test_basic_example_2(self):
        # Test basic example with a different set of words
        self.assertEqual(high("what time are we climbing up the volcano"), "volcano")

    def test_basic_example_3(self):
        # Test basic example with a smaller set of words
        self.assertEqual(high("take me to semynak"), "semynak")

    def test_single_word(self):
        # Test with a single word
        self.assertEqual(high("hello"), "hello")

    def test_multiple_words_same_score(self):
        # Test with multiple words having the same score
        self.assertEqual(high("apple banana cherry"), "cherry")

    def test_different_scores(self):
        # Test with words having different scores
        self.assertEqual(high("ant bear zebra"), "zebra")

    def test_words_with_one_letter(self):
        # Test with single-letter words
        self.assertEqual(high("a b c d e f g h i j k l m n o p q r s t u v w x y z"), "z")

    def test_empty_string(self):
        # Test with an empty string
        self.assertEqual(high(""), "")

    def test_words_with_special_characters(self):
        # Test with words containing special characters
        self.assertEqual(high("hello world"), "world")

    def test_long_words(self):
        # Test with long words to check performance
        self.assertEqual(high("pneumoultramicroscopicsilicovolcanoconiosis supercalifragilisticexpialidocious antidisestablishmentarianism"),
                         "pneumoultramicroscopicsilicovolcanoconiosis")

if __name__ == "__main__":
    unittest.main()