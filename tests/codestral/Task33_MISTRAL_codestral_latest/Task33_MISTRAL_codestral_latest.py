# from output.claude.Task33_CLAUDE_claude_3_5_sonnet_20240620 import queue_time as queue_time
# from output.codestral.Task33_MISTRAL_codestral_latest import queue_time as queue_time
# from output.gemini.Task33_GEMINI_gemini_1_5_pro_001 import queue_time as queue_time
# from output.gtp4o.Task33_OPENAI_gpt_4o import queue_time as queue_time
# from output.llama3.Task33_PERPLEXITY_llama_3_sonar_large_32k_chat import queueTime as queue_time
import unittest

class TestTask33(unittest.TestCase):

    def test_single_till(self):
        # All customers have to wait for the single till
        self.assertEqual(queue_time([5, 3, 4], 1), 12)

    def test_two_tills(self):
        # The second till finishes before the first
        self.assertEqual(queue_time([10, 2, 3, 3], 2), 10)

    def test_two_tills_different_order(self):
        # The tills have different workloads
        self.assertEqual(queue_time([2, 3, 10], 2), 12)

    def test_multiple_tills(self):
        # More tills than customers
        self.assertEqual(queue_time([5, 3, 4], 5), 5)

    def test_equal_distribution(self):
        # Evenly distributed workload
        self.assertEqual(queue_time([1, 2, 3, 4], 2), 6)

    def test_empty_queue(self):
        # No customers
        self.assertEqual(queue_time([], 1), 0)

    def test_one_customer_multiple_tills(self):
        # Single customer with multiple tills
        self.assertEqual(queue_time([5], 2), 5)

    def test_long_queue(self):
        # Long queue of customers with minimal tills
        self.assertEqual(queue_time([2, 2, 3, 3, 4, 4, 5, 5], 1), 28) # todo : fix in java

    def test_complex_distribution(self):
        # Complex distribution of customers
        self.assertEqual(queue_time([2, 3, 4, 3, 2, 1], 3), 5) # todo : fix in java

    def test_high_number_of_tills(self):
        # High number of tills, fewer customers
        self.assertEqual(queue_time([1, 1, 1, 1, 1, 1], 10), 1) # todo : fix in java

if __name__ == '__main__':
    unittest.main()