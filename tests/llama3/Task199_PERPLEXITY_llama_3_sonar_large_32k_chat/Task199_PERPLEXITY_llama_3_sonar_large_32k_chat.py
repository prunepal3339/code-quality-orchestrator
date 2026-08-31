import unittest

from output.llama3.Task199_PERPLEXITY_llama_3_sonar_large_32k_chat import Clock


class Task199_PERPLEXITY_llama_3_sonar_large_32k_chat(unittest.TestCase):

    def test_initial_time(self):
        clock = Clock(10, 30)
        self.assertEqual((clock.hours, clock.minutes), (10, 30))

    def test_add_minutes(self):
        clock = Clock(10, 30)
        clock.add_minutes(60)
        self.assertEqual((clock.hours, clock.minutes), (11, 30))

    def test_subtract_minutes(self):
        clock = Clock(10, 30)
        clock.subtract_minutes(90)
        self.assertEqual((clock.hours, clock.minutes), (9, 0))

    def test_add_overflow_minutes(self):
        clock = Clock(23, 45)
        clock.add_minutes(30)
        self.assertEqual((clock.hours, clock.minutes), (0, 15))

    def test_subtract_underflow_minutes(self):
        clock = Clock(0, 15)
        clock.subtract_minutes(30)
        self.assertEqual((clock.hours, clock.minutes), (23, 45))

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
        self.assertEqual((clock.hours, clock.minutes), (0, 0))

    def test_full_day_cycle(self):
        clock = Clock(0, 0)
        clock.add_minutes(1440)  # Adding 1440 minutes should wrap around to the same time
        self.assertEqual((clock.hours, clock.minutes), (0, 0))

    def test_negative_overflow(self):
        clock = Clock(0, 0)
        clock.subtract_minutes(1440)  # Subtracting 60 minutes from midnight should give 23:00 of the previous day
        self.assertEqual((clock.hours, clock.minutes), (1, 0))

if __name__ == '__main__':
    unittest.main()
