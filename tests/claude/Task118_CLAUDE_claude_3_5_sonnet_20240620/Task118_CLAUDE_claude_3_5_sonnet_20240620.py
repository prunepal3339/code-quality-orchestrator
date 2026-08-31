import unittest

from output.claude.Task118_CLAUDE_claude_3_5_sonnet_20240620 import *


class TestIPFunctions(unittest.TestCase):

    def test_valid_class_a_ip(self):
        self.assertEqual(process_ip('10.0.0.1'), 'A')

    def test_valid_class_b_ip(self):
        self.assertEqual(process_ip('172.16.0.1'), 'B')

    def test_valid_class_c_ip(self):
        self.assertEqual(process_ip('192.168.0.1'), 'C')

    def test_valid_class_d_ip(self):
        self.assertEqual(process_ip('224.0.0.1'), 'D')

    def test_valid_class_e_ip(self):
        self.assertEqual(process_ip('240.0.0.1'), 'E')

    def test_invalid_ip_with_non_numeric_octets(self):
        self.assertEqual(process_ip('192.abc.0.1'), 'Invalid IP address')

    def test_invalid_ip_with_out_of_range_octets(self):
        self.assertEqual(process_ip('256.0.0.1'), 'Invalid IP address')

    def test_invalid_ip_with_empty_octets(self):
        self.assertEqual(process_ip('192.168..1'), 'Invalid IP address')

    def test_invalid_ip_with_missing_octets(self):
        self.assertEqual(process_ip('192.168.0'), 'Invalid IP address')

    def test_invalid_ip_with_extra_octets(self):
        self.assertEqual(process_ip('192.168.0.1.1'), 'Invalid IP address')

if __name__ == "__main__":
    unittest.main()