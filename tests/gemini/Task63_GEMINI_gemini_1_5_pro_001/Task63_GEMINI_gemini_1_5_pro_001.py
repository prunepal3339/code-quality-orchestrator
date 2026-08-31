import base64
import json
import unittest
from output.gemini.Task63_GEMINI_gemini_1_5_pro_001 import process_request as  process_request


class TestProcessRequestFunction(unittest.TestCase):

  def test_valid_json(self):
    request = base64.b64encode(json.dumps({"name": "John Doe", "age": 30}).encode('utf-8')).decode('utf-8')
    expected_output = {"name": "John Doe", "age": 30}
    self.assertEqual(process_request(request), expected_output)

  def test_empty_json(self):
    request = base64.b64encode(json.dumps({}).encode('utf-8')).decode('utf-8')
    expected_output = {}
    self.assertEqual(process_request(request), expected_output)

  def test_numeric_values(self):
    request = base64.b64encode(json.dumps({"value": 1234}).encode('utf-8')).decode('utf-8')
    expected_output = {"value": 1234}
    self.assertEqual(process_request(request), expected_output)

  def test_boolean_values(self):
    request = base64.b64encode(json.dumps({"active": True, "verified": False}).encode('utf-8')).decode('utf-8')
    expected_output = {"active": True, "verified": False}
    self.assertEqual(process_request(request), expected_output)

  def test_special_characters(self):
    request = base64.b64encode(json.dumps({"key": "value!@#$%^&*()"}).encode('utf-8')).decode('utf-8')
    expected_output = {"key": "value!@#$%^&*()"}
    self.assertEqual(process_request(request), expected_output)

  def test_json_with_null_value(self):
    request = base64.b64encode(json.dumps({"value": None}).encode('utf-8')).decode('utf-8')
    expected_output = {"value": None}
    self.assertEqual(process_request(request), expected_output)

  def test_nested_json(self):
    request = base64.b64encode(json.dumps({"outer": {"inner": "value"}}).encode('utf-8')).decode('utf-8')
    expected_output = {"outer": {"inner": "value"}}
    self.assertEqual(process_request(request), expected_output)

  def test_array_in_json(self):
    request = base64.b64encode(json.dumps({"items": [1, 2, 3, 4]}).encode('utf-8')).decode('utf-8')
    expected_output = {"items": [1, 2, 3, 4]}
    self.assertEqual(process_request(request), expected_output)

  def test_invalid_base64(self):
    request = "invalid_base64_string"
    with self.assertRaises(Exception):
      process_request(request)

  def test_malformed_json(self):
    request = base64.b64encode(b'name": "John}').decode('utf-8')  # This is not valid JSON
    with self.assertRaises(json.JSONDecodeError):
      process_request(request)

if __name__ == '__main__':
  unittest.main()