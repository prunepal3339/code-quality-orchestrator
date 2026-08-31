import unittest


def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

class TestFindMissingNumber(unittest.TestCase):

    def test_missing_number_at_start(self):
        arr = [2, 3, 4, 5, 6]
        self.assertEqual(find_missing_number(arr), 1)

    def test_missing_number_at_end(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_missing_number(arr), 6)

    def test_missing_number_in_middle(self):
        arr = [1, 2, 4, 5, 6]
        self.assertEqual(find_missing_number(arr), 3)

    def test_missing_number_in_large_array(self):
        arr = list(range(1, 10001))
        arr.remove(5000)
        self.assertEqual(find_missing_number(arr), 5000)

    def test_single_missing_number(self):
        arr = [1]
        self.assertEqual(find_missing_number(arr), 2)

    def test_large_array_with_small_missing_number(self):
        arr = list(range(1, 10001))
        arr.remove(1)
        self.assertEqual(find_missing_number(arr), 1)

    def test_large_array_with_missing_number_at_middle(self):
        arr = list(range(1, 10001))
        arr.remove(5000)
        self.assertEqual(find_missing_number(arr), 5000)

    def test_consecutive_numbers_missing_one(self):
        arr = [10, 11, 13, 14, 15]
        self.assertEqual(find_missing_number(arr), 12)

    def test_missing_number_at_end_of_small_array(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(find_missing_number(arr), 5)

    def test_missing_number_at_start_of_small_array(self):
        arr = [2, 3, 4, 5]
        self.assertEqual(find_missing_number(arr), 1)


if __name__ == "__main__":
    unittest.main()