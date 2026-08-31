import unittest

from output.llama3.Task118_PERPLEXITY_llama_3_sonar_large_32k_chat import validate_ip


class TestIPValidation(unittest.TestCase):

    def test_valid_ipv4_class_a(self):
        self.assertTrue(validate_ip('10.0.0.1'))

    def test_valid_ipv4_class_b(self):
        self.assertTrue(validate_ip('172.16.0.1'))

    def test_valid_ipv4_class_c(self):
        self.assertTrue(validate_ip('192.168.0.1'))

    def test_valid_ipv4_class_d(self):
        self.assertTrue(validate_ip('224.0.0.1'))

    def test_valid_ipv4_class_e(self):
        self.assertTrue(validate_ip('2001:db8:ff00:42:8329:8329'))

    def test_invalid_ipv4_with_non_numeric_octets(self):
        self.assertFalse(validate_ip('192.abc.0.1'))

    def test_invalid_ipv4_with_out_of_range_octets(self):
        self.assertFalse(validate_ip('256.0.0.1'))

    def test_invalid_ipv4_with_empty_octets(self):
        self.assertFalse(validate_ip('192.168..1'))

    def test_invalid_ipv4_with_missing_octets(self):
        self.assertFalse(validate_ip('192.168.0'))

    def test_invalid_ipv4_with_extra_octets(self):
        self.assertFalse(validate_ip('192.168.0.1.1'))

if __name__ == '__main__':
    unittest.main()