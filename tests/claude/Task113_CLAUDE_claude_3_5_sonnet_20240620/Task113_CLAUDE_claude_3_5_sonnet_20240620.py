import sys
import unittest
from io import StringIO

strings = []
while True:
    s = input("Enter a string (or press Enter to finish): ")
    if s == "":
        break
    strings.append(s)

result = " ".join(strings)
print("Concatenated string:", result)



class TestStringConcatenation(unittest.TestCase):

    def setUp(self):
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_single_string(self):
        # Simulate user input
        inputs = iter(["Hello", ""])
        def mock_input(prompt):
            return next(inputs)

        # Replace input with mock_input
        global input
        input = mock_input

        # Execute the code
        strings = []
        while True:
            s = input("Enter a string (or press Enter to finish): ")
            if s == "":
                break
            strings.append(s)

        result = " ".join(strings)
        print("Concatenated string:", result)

        # Verify the result
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Concatenated string: Hello")

    def test_multiple_strings(self):
        # Simulate user input
        inputs = iter(["Hello", "World", "Python", ""])
        def mock_input(prompt):
            return next(inputs)

        # Replace input with mock_input
        global input
        input = mock_input

        # Execute the code
        strings = []
        while True:
            s = input("Enter a string (or press Enter to finish): ")
            if s == "":
                break
            strings.append(s)

        result = " ".join(strings)
        print("Concatenated string:", result)

        # Verify the result
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Concatenated string: Hello World Python")

    def test_no_strings(self):
        # Simulate user input
        inputs = iter([""])
        def mock_input(prompt):
            return next(inputs)

        # Replace input with mock_input
        global input
        input = mock_input

        # Execute the code
        strings = []
        while True:
            s = input("Enter a string (or press Enter to finish): ")
            if s == "":
                break
            strings.append(s)

        result = " ".join(strings)
        print("Concatenated string:", result)

        # Verify the result
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Concatenated string: ")

if __name__ == '__main__':
    unittest.main()