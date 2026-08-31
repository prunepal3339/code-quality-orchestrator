
import unittest


def calc(num1,num2,operator):
    num1 = float(num1)
    num2 = float(num2)
    # operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return ("Error: Division by zero")

    else:
        return ("Error: Invalid operator")


    return result



class TestCalcFunction(unittest.TestCase):

    def test_addition(self):
        # Test addition
        self.assertEqual(calc(3, 5, '+'), 8.0)

    def test_subtraction(self):
        # Test subtraction
        self.assertEqual(calc(10, 4, '-'), 6.0)

    def test_multiplication(self):
        # Test multiplication
        self.assertEqual(calc(7, 6, '*'), 42.0)

    def test_division(self):
        # Test division
        self.assertEqual(calc(9, 3, '/'), 3.0)

    def test_division_zero(self):
        # Test division by zero
        self.assertEqual(calc(5, 0, '/'), "Error: Division by zero")

    def test_invalid_operator(self):
        # Test invalid operator
        self.assertEqual(calc(5, 3, '^'), "Error: Invalid operator")

    def test_negative_numbers_addition(self):
        # Test addition with negative numbers
        self.assertEqual(calc(-3, -7, '+'), -10.0)

    def test_negative_numbers_subtraction(self):
        # Test subtraction with negative numbers
        self.assertEqual(calc(-10, -5, '-'), -5.0)

    def test_negative_numbers_multiplication(self):
        # Test multiplication with negative numbers
        self.assertEqual(calc(-4, 5, '*'), -20.0)

    def test_negative_numbers_division(self):
        # Test division with negative numbers
        self.assertEqual(calc(-10, 2, '/'), -5.0)

    def test_float_numbers(self):
        # Test operations with float numbers
        # Exact precision comparison
        self.assertEqual(calc(5.5, 2.2, '+'), 7.7)
        self.assertEqual(calc(5.5, 2.2, '*'), 12.100000000000001)

if __name__ == '__main__':
    unittest.main()