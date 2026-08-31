import unittest

from output.codestral.Task118_MISTRAL_codestral_latest import validate_ip


class TestIPValidation(unittest.TestCase):

    def test_valid_ipv4_address(self):
        self.assertTrue(validate_ip('10.0.0.1'))

    def test_valid_ipv6_address(self):
        self.assertTrue(validate_ip('2001:db8::ff00:42:8329'))

    def test_invalid_ip_with_non_numeric_octets(self):
        self.assertFalse(validate_ip('192.abc.0.1'))

    def test_invalid_ip_with_out_of_range_octets(self):
        self.assertFalse(validate_ip('256.0.0.1'))

    def test_invalid_ip_with_empty_octets(self):
        self.assertFalse(validate_ip('192.168..1'))

    def test_invalid_ip_with_missing_octets(self):
        self.assertFalse(validate_ip('192.168.0'))

    def test_invalid_ip_with_extra_octets(self):
        self.assertFalse(validate_ip('192.168.0.1.1'))

    def test_invalid_ipv6_with_invalid_format(self):
        self.assertFalse(validate_ip('2001:db8:0000:ff00:42:8329:extra'))

    def test_invalid_ipv6_with_short_length(self):
        self.assertFalse(validate_ip('2001:db8::ff00:42'))

    def test_invalid_ipv6_with_hex_out_of_range(self):
        self.assertFalse(validate_ip('2001:db8::ff00:42:12345'))

if __name__ == '__main__':
    unittest.main()