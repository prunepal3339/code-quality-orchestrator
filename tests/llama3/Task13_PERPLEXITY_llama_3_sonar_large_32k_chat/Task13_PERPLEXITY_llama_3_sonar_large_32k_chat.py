# from output.claude.Task13_CLAUDE_claude_3_5_sonnet_20240620 import is_valid_walk as is_valid_walk
# from output.codestral.Task13_MISTRAL_codestral_latest import is_valid_walk as is_valid_walk
# from output.gemini.Task13_GEMINI_gemini_1_5_pro_001 import is_valid_walk as is_valid_walk
# from output.gtp4o.Task13_OPENAI_gpt_4o import is_valid_walk as is_valid_walk
from output.llama3.Task13_PERPLEXITY_llama_3_sonar_large_32k_chat import isValidWalk as is_valid_walk
import unittest

class TestIsValidWalk(unittest.TestCase):

    def test_basic_valid_walk(self):
        walk = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
        self.assertTrue(is_valid_walk(walk))

    def test_longer_walk(self):
        walk = ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']
        self.assertFalse(is_valid_walk(walk))

    def test_single_step(self):
        walk = ['w']
        self.assertFalse(is_valid_walk(walk))

    def test_not_returning_to_start(self):
        walk = ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
        self.assertFalse(is_valid_walk(walk))

    def test_valid_walk_with_multiple_directions(self):
        walk = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's']
        self.assertTrue(is_valid_walk(walk))

    def test_valid_walk_with_repeated_directions(self):
        walk = ['n', 'e', 's', 'w', 'n', 'e', 's', 'w', 'n', 's']
        self.assertTrue(is_valid_walk(walk))

    def test_valid_walk_with_excess_steps(self):
        walk = ['n', 'n', 'n', 'n', 's', 's', 's', 's', 'e', 'w']
        self.assertTrue(is_valid_walk(walk))

    def test_valid_walk_with_different_order(self):
        walk = ['n', 's', 'n', 's', 'e', 'w', 'e', 'w', 'n', 's']
        self.assertTrue(is_valid_walk(walk))

    def test_invalid_walk_too_long(self):
        walk = ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
        self.assertFalse(is_valid_walk(walk))

    def test_valid_walk_with_balanced_steps(self):
        walk = ['n', 'n', 'e', 'e', 's', 's', 'w', 'w', 'n', 's']
        self.assertTrue(is_valid_walk(walk))

if __name__ == "__main__":
    unittest.main()