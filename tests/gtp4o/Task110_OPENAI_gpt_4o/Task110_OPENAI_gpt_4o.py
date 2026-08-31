import unittest
from unittest.mock import patch

# from output.llama3.Task110_PERPLEXITY_llama_3_sonar_large_32k_chat import validate_url
# from output.claude.Task110_CLAUDE_claude_3_5_sonnet_20240620 import is_valid_url as validate_url
# from output.gtp4o.Task110_OPENAI_gpt_4o import validate_url as validate_url
# from output.codestral.Task110_MISTRAL_codestral_latest import validate_url as validate_url
class TestURLValidation(unittest.TestCase):

    def test_valid_http_url(self):
        self.assertTrue(validate_url("http://example.com"))

    def test_valid_https_url(self):
        self.assertTrue(validate_url("https://example.com"))

    def test_valid_ftp_url(self):
        self.assertTrue(validate_url("ftp://example.com"))

    def test_valid_localhost_url(self):
        self.assertTrue(validate_url("http://localhost"))

    def test_valid_ipv4_url(self):
        self.assertTrue(validate_url("http://127.0.0.1"))

    def test_valid_ipv6_url(self):
        self.assertTrue(validate_url("http://[::1]"))

    def test_valid_url_with_port(self):
        self.assertTrue(validate_url("http://example.com:8080"))

    def test_invalid_url_missing_scheme(self):
        self.assertFalse(validate_url("example.com"))

    def test_invalid_url_with_invalid_domain(self):
        self.assertFalse(validate_url("http://-example.com"))

    def test_invalid_url_with_invalid_tld(self):
        self.assertFalse(validate_url("http://example"))

if __name__ == '__main__':
    unittest.main()