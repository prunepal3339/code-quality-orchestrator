import unittest

from output.gemini.Task199_GEMINI_gemini_1_5_pro_001 import Clock


class Task199_GEMINI_gemini_1_5_pro_001(unittest.TestCase):

    def test_initial_time(self):
        clock = Clock(10, 30)
        self.assertEqual(str(clock), "10:30")

    def test_add_minutes(self):
        clock = Clock(10, 30)
        clock += 60
        self.assertEqual(str(clock), "11:30")

    def test_subtract_minutes(self):
        clock = Clock(10, 30)
        clock -= 90
        self.assertEqual(str(clock), "09:00")

    def test_add_overflow_minutes(self):
        clock = Clock(23, 45)
        clock += 30
        self.assertEqual(str(clock), "00:15")

    def test_subtract_underflow_minutes(self):
        clock = Clock(0, 15)
        clock -= 30
        self.assertEqual(str(clock), "23:45")

    def test_equality_true(self):
        clock1 = Clock(10, 0)
        clock2 = Clock(10, 0)
        self.assertTrue(clock1 == clock2)

    def test_equality_false(self):
        clock1 = Clock(10, 0)
        clock2 = Clock(9, 0)
        self.assertFalse(clock1 == clock2)

    def test_midnight_edge_case(self):
        clock = Clock(0, 0)
        self.assertEqual(str(clock), "00:00")

    def test_full_day_cycle(self):
        clock = Clock(0, 0)
        clock += 1440
        self.assertEqual(str(clock), "00:00")

    def test_negative_overflow(self):
        clock = Clock(1, 0)
        clock -= 1440
        self.assertEqual(str(clock), "01:00")

if __name__ == '__main__':
    unittest.main()
