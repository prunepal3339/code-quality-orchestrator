import unittest


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



def testFuncc(input):
    arr = list(map(int, input.split()))
    bubble_sort(arr)
    return arr


class TestBubbleSort(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(testFuncc("4 3 2 1"), [1, 2, 3, 4])

    def test_single_element(self):
        self.assertEqual(testFuncc("5"), [5])

    def test_already_sorted(self):
        self.assertEqual(testFuncc("1 2 3 4 5"), [1, 2, 3, 4, 5])

    def test_all_elements_same(self):
        self.assertEqual(testFuncc("7 7 7 7"), [7, 7, 7, 7])

    def test_negative_numbers(self):
        self.assertEqual(testFuncc("-1 -3 -2 -4"), [-4, -3, -2, -1])

    def test_mixed_positive_and_negative(self):
        self.assertEqual(testFuncc("3 -1 0 2 -5"), [-5, -1, 0, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(testFuncc("1000 500 2000 1500"), [500, 1000, 1500, 2000])

    def test_float_numbers(self):
        self.assertEqual(testFuncc("3 2 4 1"), [1, 2, 3, 4])

    def test_mixed_integers_and_floats(self):
        self.assertEqual(testFuncc("1 2 1 2 0"), [0, 1, 1, 2, 2])

    def test_empty_input(self):
        self.assertEqual(testFuncc(""), [])

if __name__ == "__main__":
    unittest.main()