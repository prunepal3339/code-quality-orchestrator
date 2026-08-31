import unittest


class SensitiveData:
    def __init__(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

class TestSensitiveData(unittest.TestCase):

    def test_get_data_with_string(self):
        """Test get_data with a string value."""
        sensitive_data = SensitiveData("test_string")
        result = sensitive_data.get_data()
        self.assertEqual(result, "test_string")

    def test_get_data_with_integer(self):
        """Test get_data with an integer value."""
        sensitive_data = SensitiveData(12345)
        result = sensitive_data.get_data()
        self.assertEqual(result, 12345)

    def test_get_data_with_empty_string(self):
        """Test get_data with an empty string."""
        sensitive_data = SensitiveData("")
        result = sensitive_data.get_data()
        self.assertEqual(result, "")

    def test_get_data_with_list(self):
        """Test get_data with a list value."""
        sensitive_data = SensitiveData([1, 2, 3])
        result = sensitive_data.get_data()
        self.assertEqual(result, [1, 2, 3])

    def test_get_data_with_dict(self):
        """Test get_data with a dictionary value."""
        sensitive_data = SensitiveData({"key": "value"})
        result = sensitive_data.get_data()
        self.assertEqual(result, {"key": "value"})

    def test_get_data_with_float(self):
        """Test get_data with a float value."""
        sensitive_data = SensitiveData(3.14159)
        result = sensitive_data.get_data()
        self.assertEqual(result, 3.14159)

    def test_get_data_with_boolean_true(self):
        """Test get_data with a boolean True value."""
        sensitive_data = SensitiveData(True)
        result = sensitive_data.get_data()
        self.assertEqual(result, True)

    def test_get_data_with_boolean_false(self):
        """Test get_data with a boolean False value."""
        sensitive_data = SensitiveData(False)
        result = sensitive_data.get_data()
        self.assertEqual(result, False)

    def test_get_data_with_none(self):
        """Test get_data with None value."""
        sensitive_data = SensitiveData(None)
        result = sensitive_data.get_data()
        self.assertEqual(result, None)

    def test_get_data_after_reinitialization(self):
        """Test get_data after reinitializing with different data."""
        sensitive_data = SensitiveData("initial_data")
        result_initial = sensitive_data.get_data()
        self.assertEqual(result_initial, "initial_data")

        sensitive_data = SensitiveData("new_data")
        result_new = sensitive_data.get_data()
        self.assertEqual(result_new, "new_data")

# Run the tests
if __name__ == '__main__':
    unittest.main()