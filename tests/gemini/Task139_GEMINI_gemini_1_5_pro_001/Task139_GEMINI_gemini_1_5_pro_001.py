import math
import unittest


def radius(radius):
    radius = float(radius)
    area = math.pi * radius**2
    return area


class TestCircleAreaFunction(unittest.TestCase):

    def test_radius_zero(self):
        # Test with radius = 0
        result = radius(0)
        self.assertEqual(result, 0.0)

    def test_radius_one(self):
        # Test with radius = 1
        result = radius(1)
        self.assertEqual(result, math.pi * 1 ** 2)

    def test_radius_two_point_five(self):
        # Test with radius = 2.5
        result = radius(2.5)
        self.assertEqual(result, math.pi * 2.5 ** 2)

    def test_radius_ten(self):
        # Test with radius = 10
        result = radius(10)
        self.assertEqual(result, math.pi * 10 ** 2)

    def test_radius_negative(self):
        # Test with negative radius (-5)
        result = radius(-5)
        self.assertEqual(result, math.pi * (-5) ** 2)

    def test_radius_large(self):
        # Test with radius = 1000
        result = radius(1000)
        self.assertEqual(result, math.pi * 1000 ** 2)

    def test_radius_pi(self):
        # Test with floating-point radius (3.1416)
        result = radius(3.1416)
        self.assertEqual(result, math.pi * 3.1416 ** 2)

    def test_radius_small(self):
        # Test with a small radius (0.1)
        result = radius(0.1)
        self.assertEqual(result, math.pi * 0.1 ** 2)

    def test_radius_large_floating(self):
        # Test with large floating-point radius (1234.567)
        result = radius(1234.567)
        self.assertEqual(result, math.pi * 1234.567 ** 2)

    def test_radius_decimal(self):
        # Test with a precise decimal radius (9.99)
        result = radius(9.99)
        self.assertEqual(result, math.pi * 9.99 ** 2)

if __name__ == '__main__':
    unittest.main()