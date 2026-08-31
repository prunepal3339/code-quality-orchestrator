import unittest


def calculator(num1,num2,operator):
    num1 = float(num1)
    # operator = input("Enter operator (+, -, *, /): ")
    num2 = float(num2)

    if operator == "+":
        return ("Result: ", num1 + num2)
    elif operator == "-":
        return ("Result: ", num1 - num2)
    elif operator == "*":
        return ("Result: ", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            return ("Result: ", num1 / num2)
        else:
            return ("Error Division by zero is not allowed.")
    else:
        return ("Invalid operator. Please enter either +, -, * or /.")

class TestCalculatorFunction(unittest.TestCase):

    def test_addition(self):
        # Test addition with integers
        self.assertEqual(calculator(3, 5, '+'), ("Result: ", 8.0))

    def test_subtraction(self):
        # Test subtraction with integers
        self.assertEqual(calculator(10, 4, '-'), ("Result: ", 6.0))

    def test_multiplication(self):
        # Test multiplication with integers
        self.assertEqual(calculator(7, 6, '*'), ("Result: ", 42.0))

    def test_division(self):
        # Test division with integers
        self.assertEqual(calculator(9, 3, '/'), ("Result: ", 3.0))

    def test_division_zero(self):
        # Test division by zero
        self.assertEqual(calculator(5, 0, '/'), ("Error Division by zero is not allowed."))

    def test_invalid_operator(self):
        # Test invalid operator
        self.assertEqual(calculator(5, 3, '^'), ("Invalid operator. Please enter either +, -, * or /."))

    def test_negative_numbers_addition(self):
        # Test addition with negative numbers
        self.assertEqual(calculator(-3, -7, '+'), ("Result: ", -10.0))

    def test_negative_numbers_subtraction(self):
        # Test subtraction with negative numbers
        self.assertEqual(calculator(-10, -5, '-'), ("Result: ", -5.0))

    def test_negative_numbers_multiplication(self):
        # Test multiplication with negative numbers
        self.assertEqual(calculator(-4, 5, '*'), ("Result: ", -20.0))

    def test_negative_numbers_division(self):
        # Test division with negative numbers
        self.assertEqual(calculator(-10, 2, '/'), ("Result: ", -5.0))

    def test_float_numbers(self):
        # Test operations with float numbers
        self.assertEqual(calculator(5.5, 2.2, '+'), ("Result: ", 7.7))
        self.assertEqual(calculator(5.5, 2.2, '*'), ("Result: ", 12.100000000000001))

if __name__ == '__main__':
    unittest.main()

