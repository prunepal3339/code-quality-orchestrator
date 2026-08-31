import io
import unittest
from unittest.mock import patch


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            return "Invalid input. Please enter an integer."

def main():
    num1 = get_integer_input("Enter the first number: ")
    num2 = get_integer_input("Enter the second number: ")

    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2

    print(f"The sum is: {sum}")
    print(f"The difference is: {difference}")
    print(f"The product is: {product}")
class TestMainFunction(unittest.TestCase):

    def setUp(self):
        self.inputs = []
        self.patcher = patch('builtins.input', side_effect=self.mock_input)
        self.patcher.start()
        self.output = io.StringIO()
        self.patcher_output = patch('sys.stdout', new=self.output)
        self.patcher_output.start()

    def tearDown(self):
        self.patcher.stop()
        self.patcher_output.stop()

    def mock_input(self, prompt):
        return self.inputs.pop(0)

    def test_valid_inputs(self):
        self.inputs = ['5', '3']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "The sum is: 8")
        self.assertEqual(output[1], "The difference is: 2")
        self.assertEqual(output[2], "The product is: 15")

    def test_invalid_input_then_valid(self):
        self.inputs = ['abc', '4', '2']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "Invalid input. Please enter an integer.")
        self.assertEqual(output[1], "The sum is: 6")
        self.assertEqual(output[2], "The difference is: 2")
        self.assertEqual(output[3], "The product is: 8")

    def test_multiple_invalid_inputs(self):
        self.inputs = ['abc', 'def', '7', '2']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "Invalid input. Please enter an integer.")
        self.assertEqual(output[1], "Invalid input. Please enter an integer.")
        self.assertEqual(output[2], "The sum is: 9")
        self.assertEqual(output[3], "The difference is: 5")
        self.assertEqual(output[4], "The product is: 14")

    def test_negative_numbers(self):
        self.inputs = ['-3', '-2']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "The sum is: -5")
        self.assertEqual(output[1], "The difference is: -1")
        self.assertEqual(output[2], "The product is: 6")

    def test_zero_values(self):
        self.inputs = ['0', '0']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "The sum is: 0")
        self.assertEqual(output[1], "The difference is: 0")
        self.assertEqual(output[2], "The product is: 0")

    def test_large_numbers(self):
        self.inputs = ['100000', '99999']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "The sum is: 199999")
        self.assertEqual(output[1], "The difference is: 1")
        self.assertEqual(output[2], "The product is: 9999900000")

    def test_float_input(self):
        self.inputs = ['3.5', '4']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "Invalid input. Please enter an integer.")
        self.assertEqual(output[1], "The sum is: 7")
        self.assertEqual(output[2], "The difference is: 3")
        self.assertEqual(output[3], "The product is: 12")

    def test_empty_input(self):
        self.inputs = ['', '5']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "Invalid input. Please enter an integer.")
        self.assertEqual(output[1], "The sum is: 5")
        self.assertEqual(output[2], "The difference is: 0")
        self.assertEqual(output[3], "The product is: 0")

    def test_special_characters(self):
        self.inputs = ['@#!$', '2']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "Invalid input. Please enter an integer.")
        self.assertEqual(output[1], "The sum is: 2")
        self.assertEqual(output[2], "The difference is: 0")
        self.assertEqual(output[3], "The product is: 0")

    def test_multiple_values(self):
        self.inputs = ['1', '2', '3']
        main()
        output = self.output.getvalue().strip().split('\n')
        self.assertEqual(output[0], "The sum is: 3")
        self.assertEqual(output[1], "The difference is: -1")
        self.assertEqual(output[2], "The product is: 2")

if __name__ == '__main__':
    unittest.main()

