import unittest


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Invalid operator"

# Test Class
class TestCalculateFunction(unittest.TestCase):

    def test_addition(self):
        # Test addition with integers
        self.assertEqual(calculate(3, 5, '+'), 8)

    def test_subtraction(self):
        # Test subtraction with integers
        self.assertEqual(calculate(10, 4, '-'), 6)

    def test_multiplication(self):
        # Test multiplication with integers
        self.assertEqual(calculate(7, 6, '*'), 42)

    def test_division(self):
        # Test division with integers
        self.assertEqual(calculate(9, 3, '/'), 3)

    def test_invalid_operator(self):
        # Test invalid operator
        self.assertEqual(calculate(5, 3, '^'), "Invalid operator")

    def test_negative_numbers_addition(self):
        # Test addition with negative numbers
        self.assertEqual(calculate(-3, -7, '+'), -10)

    def test_negative_numbers_subtraction(self):
        # Test subtraction with negative numbers
        self.assertEqual(calculate(-10, -5, '-'), -5)

    def test_negative_numbers_multiplication(self):
        # Test multiplication with negative numbers
        self.assertEqual(calculate(-4, 5, '*'), -20)

    def test_negative_numbers_division(self):
        # Test division with negative numbers
        self.assertEqual(calculate(-10, 2, '/'), -5)

    def test_float_numbers(self):
        # Test operations with float numbers
        self.assertEqual(calculate(5.5, 2.2, '+'), 7.7)
        self.assertEqual(calculate(5.5, 2.2, '*'), 12.100000000000001)

if __name__ == '__main__':
    unittest.main()