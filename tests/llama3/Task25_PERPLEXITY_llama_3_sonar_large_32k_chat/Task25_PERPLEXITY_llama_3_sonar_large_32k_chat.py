# from output.claude.Task25_CLAUDE_claude_3_5_sonnet_20240620 import number as validate_pin
# from output.codestral.Task25_MISTRAL_codestral_latest import number as validate_pin
# from output.gemini.Task25_GEMINI_gemini_1_5_pro_001 import number as validate_pin
# from output.gtp4o.Task25_OPENAI_gpt_4o import number as validate_pin
# from output.llama3.Task25_PERPLEXITY_llama_3_sonar_large_32k_chat import number_lines as validate_pin
import unittest


class TestPinValidation(unittest.TestCase):

    def test_valid_4_digit_pin(self):
        self.assertTrue(validate_pin("1234"))

    def test_valid_6_digit_pin(self):
        self.assertTrue(validate_pin("123456"))

    def test_invalid_length_pin_too_short(self):
        self.assertFalse(validate_pin("123"))

    def test_invalid_length_pin_too_long(self):
        self.assertFalse(validate_pin("1234567"))

    def test_invalid_pin_with_letters(self):
        self.assertFalse(validate_pin("a234"))

    def test_invalid_pin_with_special_characters(self):
        self.assertFalse(validate_pin("12@4"))

    def test_valid_6_digit_pin_with_leading_zeros(self):
        self.assertTrue(validate_pin("000123"))

    def test_valid_4_digit_pin_with_leading_zeros(self):
        self.assertTrue(validate_pin("0001"))

    def test_invalid_pin_with_spaces(self):
        self.assertFalse(validate_pin("12 34"))

    def test_empty_pin(self):
        self.assertFalse(validate_pin(""))

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()