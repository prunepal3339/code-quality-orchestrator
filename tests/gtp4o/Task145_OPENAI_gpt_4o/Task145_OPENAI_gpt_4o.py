import unittest


def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

class TestMaxSubarraySum(unittest.TestCase):
    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_subarray_sum(arr), 15)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(max_subarray_sum(arr), -1)

    def test_mixed_numbers(self):
        arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_sum(arr), 9)

    def test_single_element(self):
        arr = [42]
        self.assertEqual(max_subarray_sum(arr), 42)

    def test_all_zeroes(self):
        arr = [0, 0, 0, 0, 0]
        self.assertEqual(max_subarray_sum(arr), 0)

    def test_large_array(self):
        arr = [1] * 1000  # Array of 1000 ones
        self.assertEqual(max_subarray_sum(arr), 1000)

    def test_alternating_signs(self):
        arr = [3, -1, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_sum(arr), 8)

    def test_large_positive_and_negative_numbers(self):
        arr = [10, -1, -1, 10, -1, 10, -1]
        self.assertEqual(max_subarray_sum(arr), 27)

    def test_subarray_at_the_end(self):
        arr = [1, -2, -3, 4, 5]
        self.assertEqual(max_subarray_sum(arr), 9)

    def test_subarray_at_the_start(self):
        arr = [6, -1, -2, 1, 2]
        self.assertEqual(max_subarray_sum(arr), 6)

# Run the tests
if __name__ == '__main__':
    unittest.main()