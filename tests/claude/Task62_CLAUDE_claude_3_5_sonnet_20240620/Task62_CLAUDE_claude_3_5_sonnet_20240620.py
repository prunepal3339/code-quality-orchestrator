from output.claude.Task62_CLAUDE_claude_3_5_sonnet_20240620 import parse_json_and_get_root as parse_json_and_get_root
# from output.gemini.Task62_GEMINI_gemini_1_5_pro_001 import get_root_element as parse_json_and_get_root
# from output.gtp4o.Task62_OPENAI_gpt_4o import get_root_element as parse_json_and_get_root
import unittest


class TestParseJsonAndGetRootFunction(unittest.TestCase):

    def test_valid_json(self):
        json_str = '{"name": "John", "age": 30, "city": "New York"}'
        self.assertEqual(parse_json_and_get_root(json_str), {"name": "John", "age": 30, "city": "New York"})

    def test_empty_json(self):
        json_str = '{}'
        self.assertEqual(parse_json_and_get_root(json_str), {})

    def test_json_with_array(self):
        json_str = '[1, 2, 3, 4]'
        self.assertEqual(parse_json_and_get_root(json_str), [1, 2, 3, 4])

    def test_json_with_nested_objects(self):
        json_str = '{"person": {"name": "Alice", "age": 25}, "city": "Wonderland"}'
        self.assertEqual(parse_json_and_get_root(json_str), {"person": {"name": "Alice", "age": 25}, "city": "Wonderland"})

    def test_json_with_boolean_values(self):
        json_str = '{"active": true, "verified": false}'
        self.assertEqual(parse_json_and_get_root(json_str), {"active": True, "verified": False})

    def test_json_with_null_value(self):
        json_str = '{"value": null}'
        self.assertEqual(parse_json_and_get_root(json_str), {"value": None})

    def test_malformed_json_missing_bracket(self):
        json_str = '{"name": "John", "age": 30, "city": "New York"'
        self.assertIsNone(parse_json_and_get_root(json_str))

    def test_malformed_json_unexpected_comma(self):
        json_str = '{"name": "John", "age": 30,}'
        self.assertIsNone(parse_json_and_get_root(json_str))

    def test_malformed_json_unquoted_key(self):
        json_str = '{name: "John", "age": 30}'
        self.assertIsNone(parse_json_and_get_root(json_str))

    def test_invalid_json_type(self):
        json_str = 'Just a string, not JSON'
        self.assertIsNone(parse_json_and_get_root(json_str))

if __name__ == '__main__':
    unittest.main()