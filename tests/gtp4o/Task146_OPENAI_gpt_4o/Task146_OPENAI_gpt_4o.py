# Program in Python
import unittest


def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    return total_sum - array_sum

class TestFindMissingNumber(unittest.TestCase):

    def test_missing_number_at_start(self):
        arr = [2, 3, 4, 5, 6]
        n = 6
        self.assertEqual(find_missing_number(arr, n), 1)

    def test_missing_number_at_end(self):
        arr = [1, 2, 3, 4, 5]
        n = 6
        self.assertEqual(find_missing_number(arr, n), 6)

    def test_missing_number_in_middle(self):
        arr = [1, 2, 4, 5, 6]
        n = 6
        self.assertEqual(find_missing_number(arr, n), 3)

    def test_missing_number_in_large_array(self):
        arr = list(range(1, 10001))
        arr.remove(5000)
        self.assertEqual(find_missing_number(arr, 10000), 5000)

    def test_single_missing_number(self):
        arr = [1]
        n = 2
        self.assertEqual(find_missing_number(arr, n), 2)

    def test_large_array_with_small_missing_number(self):
        arr = list(range(2, 10001))
        n = 10000
        self.assertEqual(find_missing_number(arr, n), 1)

    def test_large_array_with_missing_number_at_middle(self):
        arr = list(range(1, 10001))
        arr.remove(5000)
        self.assertEqual(find_missing_number(arr, 10000), 5000)

    def test_consecutive_numbers_missing_one(self):
        arr = [10, 11, 13, 14, 15]
        n = 15
        self.assertEqual(find_missing_number(arr, n), 12)


    def test_missing_number_at_end_of_small_array(self):
        arr = [1, 2, 3, 4]
        n = 5
        self.assertEqual(find_missing_number(arr, n), 5)

    def test_missing_number_at_start_of_small_array(self):
        arr = [2, 3, 4, 5]
        n = 5
        self.assertEqual(find_missing_number(arr, n), 1)

if __name__ == "__main__":
    unittest.main()