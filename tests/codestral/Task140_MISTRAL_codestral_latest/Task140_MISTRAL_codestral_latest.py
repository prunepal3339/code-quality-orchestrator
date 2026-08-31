import unittest


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

class TestcalculateFunction(unittest.TestCase):

    def test_addition(self):
        # Test addition
        self.assertEqual(calculate(3, 5, '+'), 8.0)

    def test_subtraction(self):
        # Test subtraction
        self.assertEqual(calculate(10, 4, '-'), 6.0)

    def test_multiplication(self):
        # Test multiplication
        self.assertEqual(calculate(7, 6, '*'), 42.0)

    def test_division(self):
        # Test division
        self.assertEqual(calculate(9, 3, '/'), 3.0)

    def test_division_zero(self):
        # Test division by zero
        self.assertEqual(calculate(5, 0, '/'), "Error: Division by zero")

    def test_invalid_operator(self):
        # Test invalid operator
        self.assertEqual(calculate(5, 3, '^'), "Error: Invalid operator")

    def test_negative_numbers_addition(self):
        # Test addition with negative numbers
        self.assertEqual(calculate(-3, -7, '+'), -10.0)

    def test_negative_numbers_subtraction(self):
        # Test subtraction with negative numbers
        self.assertEqual(calculate(-10, -5, '-'), -5.0)

    def test_negative_numbers_multiplication(self):
        # Test multiplication with negative numbers
        self.assertEqual(calculate(-4, 5, '*'), -20.0)

    def test_negative_numbers_division(self):
        # Test division with negative numbers
        self.assertEqual(calculate(-10, 2, '/'), -5.0)

    def test_float_numbers(self):
        # Test operations with float numbers
        # Exact precision comparison
        self.assertEqual(calculate(5.5, 2.2, '+'), 7.7)
        self.assertEqual(calculate(5.5, 2.2, '*'), 12.100000000000001)

if __name__ == '__main__':
    unittest.main()