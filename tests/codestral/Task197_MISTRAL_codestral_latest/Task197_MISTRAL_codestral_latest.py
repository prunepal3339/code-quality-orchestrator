import unittest

from output.codestral.Task197_MISTRAL_codestral_latest import Solution

class Task197_MISTRAL_codestral_latest(unittest.TestCase):

    def test_rand_point_within_circle(self):
        solution = Solution(1.0, 0.0, 0.0)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertTrue(x * x + y * y <= 1.0, "Point should be within the circle of radius 1.")

    def test_rand_point_center_offset(self):
        solution = Solution(1.0, 1.0, 1.0)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertTrue((x - 1) * (x - 1) + (y - 1) * (y - 1) <= 1.0, "Point should be within the circle centered at (1, 1).")

    def test_rand_point_large_radius(self):
        solution = Solution(100.0, 0.0, 0.0)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertTrue(x * x + y * y <= 10000.0, "Point should be within the circle of radius 100.")

    def test_rand_point_small_radius(self):
        solution = Solution(0.1, 0.0, 0.0)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertTrue(x * x + y * y <= 0.01, "Point should be within the circle of very small radius.")

    def test_rand_point_negative_center(self):
        solution = Solution(1.0, -5.0, -5.0)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertTrue((x + 5) * (x + 5) + (y + 5) * (y + 5) <= 1.0, "Point should be within the circle centered at (-5, -5).")

    def test_rand_point_large_center(self):
        solution = Solution(1.0, 1e6, 1e6)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertTrue((x - 1e6) * (x - 1e6) + (y - 1e6) * (y - 1e6) <= 1.0, "Point should be within the circle centered at (1e6, 1e6).")

    def test_rand_point_zero_radius(self):
        solution = Solution(0.0, 0.0, 0.0)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertEqual(0.0, x, "Point should be exactly at the center.")
            self.assertEqual(0.0, y, "Point should be exactly at the center.")

    def test_rand_point_high_radius(self):
        solution = Solution(1e8, 0.0, 0.0)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertTrue(x * x + y * y <= 1e16, "Point should be within the circle of radius 1e8.")

    def test_rand_point_non_zero_center(self):
        solution = Solution(10.0, 10.0, 10.0)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertTrue((x - 10) * (x - 10) + (y - 10) * (y - 10) <= 100.0, "Point should be within the circle centered at (10, 10).")

    def test_rand_point_multiple_calls(self):
        solution = Solution(50.0, 0.0, 0.0)
        for _ in range(100):
            x, y = solution.randPoint()
            self.assertTrue(x * x + y * y <= 2500.0, "Point should be within the circle of radius 50.")

if __name__ == "__main__":
    unittest.main()
