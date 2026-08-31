import unittest


def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

class TestMergeSortedArrays(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertEqual(merge_sorted_arrays([], []), [])

    def test_one_empty_array(self):
        self.assertEqual(merge_sorted_arrays([], [1, 3, 5]), [1, 3, 5])
        self.assertEqual(merge_sorted_arrays([2, 4, 6], []), [2, 4, 6])

    def test_single_element_arrays(self):
        self.assertEqual(merge_sorted_arrays([1], [1]), [1, 1])
        self.assertEqual(merge_sorted_arrays([1], [2]), [1, 2])

    def test_different_sizes_with_all_smaller_elements(self):
        self.assertEqual(merge_sorted_arrays([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_some_overlapping_elements(self):
        self.assertEqual(merge_sorted_arrays([1, 3, 5], [2, 3, 4]), [1, 2, 3, 3, 4, 5])

    def test_all_elements_same(self):
        self.assertEqual(merge_sorted_arrays([2, 2, 2], [2, 2, 2]), [2, 2, 2, 2, 2, 2])

    def test_interleaving_elements(self):
        self.assertEqual(merge_sorted_arrays([1, 3, 5, 7], [2, 4, 6, 8]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_large_element_diff(self):
        self.assertEqual(merge_sorted_arrays([1, 2], [1000, 2000, 3000]), [1, 2, 1000, 2000, 3000])

    def test_reverse_order_arrays(self):
        self.assertEqual(merge_sorted_arrays([8, 6, 4, 9, 7, 5], [4, 5, 6, 7, 8, 9]), [4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])

if __name__ == '__main__':
    unittest.main()