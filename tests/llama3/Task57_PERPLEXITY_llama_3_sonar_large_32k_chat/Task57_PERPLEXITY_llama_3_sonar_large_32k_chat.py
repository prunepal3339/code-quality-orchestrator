import unittest


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_two(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_three(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_four(self):
        self.assertEqual(factorial(4), 24)

    def test_factorial_five(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_six(self):
        self.assertEqual(factorial(6), 720)

    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_number(self):
        with self.assertRaises(RecursionError):
            factorial(-1)

    def test_factorial_string_input(self):
        with self.assertRaises(TypeError):
            factorial("string")

if __name__ == "__main__":
    unittest.main()