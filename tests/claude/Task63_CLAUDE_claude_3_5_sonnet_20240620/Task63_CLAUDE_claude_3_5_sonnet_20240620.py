import base64
import json

from output.claude.Task63_CLAUDE_claude_3_5_sonnet_20240620 import process_request as process_request
from output.codestral.Task63_MISTRAL_codestral_latest import process_request as process_request
# from output.gemini.Task63_GEMINI_gemini_1_5_pro_001 import process_request as process_request
# from output.gtp4o.Task63_OPENAI_gpt_4o import process_request as process_request
# from output.llama3.Task63_PERPLEXITY_llama_3_sonar_large_32k_chat import process_request as process_request
import unittest


class TestProcessRequestFunction(unittest.TestCase):

    def test_valid_json(self):
        raw_data = "eyJuYW1lIjogIkpvaG4gRG9lIiwgImFnZSI6IDMwfQ=="
        expected_output = {"name": "John Doe", "age": 30}
        self.assertEqual(process_request(raw_data), expected_output)

    def test_empty_input(self):
        raw_data = ""
        self.assertRaises(Exception, process_request, raw_data)

    def test_invalid_base64(self):
        raw_data = "invalid_base64_string"
        self.assertRaises(Exception, process_request, raw_data)

    def test_malformed_json(self):
        # Base64 encoded string that decodes to 'name": "John}' which is malformed JSON
        raw_data = base64.b64encode(b'name": "John}').decode('utf-8')
        self.assertRaises(json.JSONDecodeError, process_request, raw_data)


    def test_base64_of_empty_json(self):
        raw_data = base64.b64encode(json.dumps({}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(raw_data), {})

    def test_json_with_special_characters(self):
        raw_data = base64.b64encode(json.dumps({"key": "value_with_special_characters_!@#$%^&*()"}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(raw_data), {"key": "value_with_special_characters_!@#$%^&*()"})

    def test_json_with_numeric_values(self):
        raw_data = base64.b64encode(json.dumps({"value": 1234}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(raw_data), {"value": 1234})

    def test_json_with_boolean_values(self):
        raw_data = base64.b64encode(json.dumps({"active": True, "verified": False}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(raw_data), {"active": True, "verified": False})

    def test_json_with_null_value(self):
        raw_data = base64.b64encode(json.dumps({"value": None}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(raw_data), {"value": None})

    def test_nested_json(self):
        raw_data = base64.b64encode(json.dumps({"outer": {"inner": "value"}}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(raw_data), {"outer": {"inner": "value"}})

if __name__ == '__main__':
    unittest.main()