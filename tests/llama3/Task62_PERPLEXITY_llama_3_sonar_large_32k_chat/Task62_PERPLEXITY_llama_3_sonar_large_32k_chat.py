import unittest
import json

from output.llama3.Task62_PERPLEXITY_llama_3_sonar_large_32k_chat import get_root_element


class TestGetRootElementFunction(unittest.TestCase):

    def test_valid_json_object(self):
        json_str = '{"name": "John", "age": 30, "city": "New York"}'
        self.assertEqual(get_root_element(json_str), 'dict')

    def test_empty_json_object(self):
        json_str = '{}'
        self.assertEqual(get_root_element(json_str), 'dict')

    def test_json_array(self):
        json_str = '[1, 2, 3, 4]'
        self.assertEqual(get_root_element(json_str), 'list')

    def test_json_with_nested_objects(self):
        json_str = '{"person": {"name": "Alice", "age": 25}, "city": "Wonderland"}'
        self.assertEqual(get_root_element(json_str), 'dict')

    def test_json_with_boolean_values(self):
        json_str = '{"active": true, "verified": false}'
        self.assertEqual(get_root_element(json_str), 'dict')

    def test_json_with_null_value(self):
        json_str = '{"value": null}'
        self.assertEqual(get_root_element(json_str), 'dict')

    def test_malformed_json_missing_bracket(self):
        json_str = '{"name": "John", "age": 30, "city": "New York"'
        self.assertIsNone(get_root_element(json_str))

    def test_malformed_json_unexpected_comma(self):
        json_str = '{"name": "John", "age": 30,}'
        self.assertIsNone(get_root_element(json_str))

    def test_malformed_json_unquoted_key(self):
        json_str = '{name: "John", "age": 30}'
        self.assertIsNone(get_root_element(json_str))

    def test_invalid_json_type(self):
        json_str = 'Just a string, not JSON'
        self.assertIsNone(get_root_element(json_str))

if __name__ == '__main__':
    unittest.main()