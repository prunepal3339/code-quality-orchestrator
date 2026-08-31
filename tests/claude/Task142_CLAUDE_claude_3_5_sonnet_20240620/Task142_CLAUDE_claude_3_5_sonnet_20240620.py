import unittest


import unittest

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class TestGCD(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_same_numbers(self):
        self.assertEqual(gcd(7, 7), 7)

    def test_one_number_zero(self):
        self.assertEqual(gcd(0, 15), 15)
        self.assertEqual(gcd(15, 0), 15)

    def test_prime_numbers(self):
        self.assertEqual(gcd(13, 17), 1)

    def test_one_number_is_one(self):
        self.assertEqual(gcd(1, 25), 1)
        self.assertEqual(gcd(25, 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(gcd(-48, -18),-6)
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), -6)

    def test_large_numbers(self):
        self.assertEqual(gcd(123456, 7890), 6)

    def test_coprime_numbers(self):
        self.assertEqual(gcd(35, 64), 1)

    def test_small_and_large_numbers(self):
        self.assertEqual(gcd(7, 1001), 7)

    def test_identical_large_numbers(self):
        self.assertEqual(gcd(1000000, 1000000), 1000000)


if __name__ == "__main__":
    unittest.main()