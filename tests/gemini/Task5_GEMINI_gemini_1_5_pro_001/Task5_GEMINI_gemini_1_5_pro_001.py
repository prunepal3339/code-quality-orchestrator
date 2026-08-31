from output.gemini.Task5_GEMINI_gemini_1_5_pro_001 import persistence

import unittest


class TestPersistence(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(persistence(39), 3)  # Example: 3 steps

    def test_case2(self):
        self.assertEqual(persistence(999), 4)  # Example: 4 steps

    def test_case3(self):
        self.assertEqual(persistence(4), 0)  # Single digit, no steps needed

    def test_case4(self):
        self.assertEqual(persistence(25), 2)  # 2 steps to reach a single digit (25 -> 10 -> 0)

    def test_case5(self):
        self.assertEqual(persistence(77), 4)  # 2 steps needed (77 -> 49 -> 36 -> 0)

    def test_case6(self):
        self.assertEqual(persistence(8), 0)  # Single digit, no steps needed

    def test_case7(self):
        self.assertEqual(persistence(10), 1)  # 1 step needed (10 -> 0)

    def test_case8(self):
        self.assertEqual(persistence(123), 1)  # 1 step needed (123 -> 6)

    def test_case9(self):
        self.assertEqual(persistence(6788), 6)  # 6 steps needed (6788 -> 2688 -> 768 -> 336 -> 54 -> 20 -> 0)

    def test_case10(self):
        self.assertEqual(persistence(9909), 1)  # 2 steps needed (1111 -> 1 -> 1)

if __name__ == '__main__':
    unittest.main()

