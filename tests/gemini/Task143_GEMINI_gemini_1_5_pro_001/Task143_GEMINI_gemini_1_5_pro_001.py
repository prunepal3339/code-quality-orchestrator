import unittest


def sort_array(arr):
  arr.sort()
  return arr


class TestSortArray(unittest.TestCase):

  def test_basic(self):
    self.assertEqual(sort_array([4, 3, 2, 1]), [1, 2, 3, 4])

  def test_single_element(self):
    self.assertEqual(sort_array([5]), [5])

  def test_already_sorted(self):
    self.assertEqual(sort_array([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

  def test_all_elements_same(self):
    self.assertEqual(sort_array([7, 7, 7, 7]), [7, 7, 7, 7])

  def test_negative_numbers(self):
    self.assertEqual(sort_array([-1, -3, -2, -4]), [-4, -3, -2, -1])

  def test_mixed_positive_and_negative(self):
    self.assertEqual(sort_array([3, -1, 0, 2, -5]), [-5, -1, 0, 2, 3])

  def test_large_numbers(self):
    self.assertEqual(sort_array([1000, 500, 2000, 1500]), [500, 1000, 1500, 2000])

  def test_float_numbers(self):
    self.assertEqual(sort_array([3.5, 2.1, 4.7, 1.9]), [1.9, 2.1, 3.5, 4.7])

  def test_mixed_integers_and_floats(self):
    self.assertEqual(sort_array([1, 2.5, 1.5, 2, 0.5]), [0.5, 1, 1.5, 2, 2.5])

  def test_empty_input(self):
    self.assertEqual(sort_array([]), [])

if __name__ == "__main__":
  unittest.main()