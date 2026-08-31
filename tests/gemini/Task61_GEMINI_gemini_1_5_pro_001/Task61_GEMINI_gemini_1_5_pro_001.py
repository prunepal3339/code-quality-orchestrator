# from output.claude.Task61_CLAUDE_claude_3_5_sonnet_20240620 import get_root_element as get_root_element
# from output.codestral.Task61_MISTRAL_codestral_latest import get_root_element as get_root_element
# from output.gemini.Task61_GEMINI_gemini_1_5_pro_001 import get_root_element as get_root_element
# from output.gtp4o.Task61_OPENAI_gpt_4o import get_root_element as get_root_element
# from output.llama3.Task61_PERPLEXITY_llama_3_sonar_large_32k_chat import get_root_element as get_root_element
import unittest
import xml.etree.ElementTree as ET

class TestGetRootElementFunction(unittest.TestCase):

    def test_basic_xml(self):
        xml_str = '<root><child1>Content</child1><child2 attr="value"/></root>'
        self.assertEqual(get_root_element(xml_str), 'root')

    def test_single_element_xml(self):
        xml_str = '<single/>'
        self.assertEqual(get_root_element(xml_str), 'single')

    def test_nested_elements(self):
        xml_str = '<parent><child><subchild/></child></parent>'
        self.assertEqual(get_root_element(xml_str), 'parent')

    def test_empty_document(self):
        xml_str = '<empty></empty>'
        self.assertEqual(get_root_element(xml_str), 'empty')

    def test_self_closing_tag(self):
        xml_str = '<selfclosing attr="value"/>'
        self.assertEqual(get_root_element(xml_str), 'selfclosing')

    def test_xml_with_attributes(self):
        xml_str = '<root attr="value"><child/></root>'
        self.assertEqual(get_root_element(xml_str), 'root')

    def test_multiple_root_elements(self):
        xml_str = '<root1/><root2/>'
        with self.assertRaises(ET.ParseError):
            get_root_element(xml_str)

    def test_large_xml(self):
        xml_str = '<root>' + '<child>' * 1000 + '</child>' * 1000 + '</root>'
        self.assertEqual(get_root_element(xml_str), 'root')

    def test_malformed_xml(self):
        xml_str = '<root><child></root>'
        with self.assertRaises(ET.ParseError):
            get_root_element(xml_str)

    def test_xml_with_namespaces(self):
        xml_str = '<ns:root xmlns:ns="http://example.com"><ns:child/></ns:root>'
        self.assertEqual(get_root_element(xml_str), '{http://example.com}root')

if __name__ == '__main__':
    unittest.main()