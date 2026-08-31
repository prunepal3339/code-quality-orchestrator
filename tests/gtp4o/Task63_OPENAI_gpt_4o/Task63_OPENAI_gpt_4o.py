import base64
import json
import unittest
from output.gtp4o.Task63_OPENAI_gpt_4o import process_request as process_request


class TestProcessRequest(unittest.TestCase):

    def test_simple_key_value(self):
        req = base64.b64encode(json.dumps({"key": "value"}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(req), {"key": "value"})

    def test_multiple_key_value(self):
        req = base64.b64encode(json.dumps({"name": "John", "age": 30}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(req), {"name": "John", "age": 30})

    def test_nested_json(self):
        req = base64.b64encode(json.dumps({"user": {"name": "Alice", "age": 25}}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(req), {"user": {"name": "Alice", "age": 25}})

    def test_list_in_json(self):
        req = base64.b64encode(json.dumps({"numbers": [1, 2, 3, 4]}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(req), {"numbers": [1, 2, 3, 4]})

    def test_empty_json(self):
        req = base64.b64encode(json.dumps({}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(req), {})

    def test_boolean_values(self):
        req = base64.b64encode(json.dumps({"is_active": True, "is_admin": False}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(req), {"is_active": True, "is_admin": False})

    def test_null_value(self):
        req = base64.b64encode(json.dumps({"value": None}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(req), {"value": None})

    def test_numeric_values(self):
        req = base64.b64encode(json.dumps({"integer": 100, "float": 10.5}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(req), {"integer": 100, "float": 10.5})

    def test_special_characters(self):
        req = base64.b64encode(json.dumps({"greeting": "Hello, World!"}).encode('utf-8')).decode('utf-8')
        self.assertEqual(process_request(req), {"greeting": "Hello, World!"})

    def test_malformed_base64(self):
        req = "InvalidBase64String"
        with self.assertRaises(base64.binascii.Error):
            process_request(req)

if __name__ == '__main__':
    unittest.main()