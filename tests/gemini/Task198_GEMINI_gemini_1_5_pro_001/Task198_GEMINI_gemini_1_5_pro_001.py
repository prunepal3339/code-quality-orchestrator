import unittest
from collections import Counter

import random
class Solution:
    def rand10(self):
        while True:
            num = (rand7() - 1) * 7 + rand7()  # Generate a number between 1 and 49
            if num <= 40:
                return (num - 1) % 10 + 1  # Map to 1-10

def rand7():
    return random.randint(1, 7)

class Task199Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rand10_uniform_distribution(self):
        n = 100000
        counts = Counter(self.solution.rand10() for _ in range(n))
        for value in range(1, 11):
            self.assertTrue(counts[value] >= n / 15 and counts[value] <= n / 7,
                            "The distribution of rand10() is not uniform.")

    def test_rand10_single_call(self):
        possible_results = {self.solution.rand10() for _ in range(100)}
        for value in range(1, 11):
            self.assertIn(value, possible_results,
                          "rand10() should be able to produce all numbers between 1 and 10.")

    def test_rand10_multiple_calls(self):
        for _ in range(10):
            result = self.solution.rand10()
            self.assertTrue(1 <= result <= 10,
                            "rand10() should return a value between 1 and 10 on multiple calls.")

    def test_rand10_performance(self):
        import time
        start_time = time.time()
        n = 1000000
        for _ in range(n):
            self.solution.rand10()
        elapsed_time = time.time() - start_time
        self.assertTrue(elapsed_time < 2000, "rand10() performance should be within acceptable limits.")

    def test_rand10_consistency(self):
        first_result = self.solution.rand10()
        for _ in range(100):
            result = self.solution.rand10()
            self.assertTrue(1 <= result <= 10, "rand10() should be consistent in its output.")

    def test_rand10_boundary_conditions(self):
        for _ in range(1000):
            result = self.solution.rand10()
            self.assertTrue(1 <= result <= 10, "rand10() should always return values within the range 1 to 10.")

    def test_rand10_randomness(self):
        result_set = {self.solution.rand10() for _ in range(1000)}
        self.assertEqual(len(result_set), 10, "rand10() should produce all numbers between 1 and 10 over time.")

    def test_rand10_extreme_values(self):
        for _ in range(1000):
            result = self.solution.rand10()
            self.assertTrue(1 <= result <= 10, "rand10() should never produce values outside the range 1 to 10.")

    def test_rand10_multiple_executions(self):
        for _ in range(100):
            result = self.solution.rand10()
            self.assertTrue(1 <= result <= 10, "rand10() should behave correctly on repeated executions.")

    def test_rand10_edge_case_check(self):
        edge_cases = set()
        for _ in range(10000):
            result = self.solution.rand10()
            if result == 1 or result == 10:
                edge_cases.add(result)
        self.assertTrue(1 in edge_cases and 10 in edge_cases, "rand10() should be able to produce edge values 1 and 10.")

if __name__ == "__main__":
    unittest.main()
