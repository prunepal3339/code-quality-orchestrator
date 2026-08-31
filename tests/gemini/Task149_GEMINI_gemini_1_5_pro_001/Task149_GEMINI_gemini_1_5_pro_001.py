# from output.codestral.Task149_MISTRAL_codestral_latest import *
# from output.gemini.Task149_GEMINI_gemini_1_5_pro_001 import *
# from output.gtp4o.Task149_OPENAI_gpt_4o import *
# from output.llama3.Task149_PERPLEXITY_llama_3_sonar_large_32k_chat import *


class TestQueue:
    def __init__(self):
        self.run_tests()

    def test_enqueue_and_peek(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.peek() == 1, "Failed Test Case 1: test_enqueue_and_peek"

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1, "Failed Test Case 2: test_dequeue"
        assert queue.peek() == 2, "Failed Test Case 3: test_dequeue"

    def test_empty_queue(self):
        queue = Queue()
        # assert queue.is_empty() is True, "Failed Test Case 4: test_empty_queue"
        queue.enqueue(1)
        # assert queue.is_empty() is False, "Failed Test Case 5: test_empty_queue"

    def test_peek_empty_queue(self):
        queue = Queue()
        assert queue.peek() is None, "Failed Test Case 6: test_peek_empty_queue"

    def test_dequeue_empty_queue(self):
        queue = Queue()
        assert queue.dequeue() is None, "Failed Test Case 7: test_dequeue_empty_queue"

    def test_multiple_enqueue_and_dequeue(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        assert queue.dequeue() == 10, "Failed Test Case 8: test_multiple_enqueue_and_dequeue"
        assert queue.dequeue() == 20, "Failed Test Case 9: test_multiple_enqueue_and_dequeue"
        assert queue.dequeue() == 30, "Failed Test Case 10: test_multiple_enqueue_and_dequeue"

    def run_tests(self):
        self.test_enqueue_and_peek()
        self.test_dequeue()
        self.test_empty_queue()
        self.test_peek_empty_queue()
        self.test_dequeue_empty_queue()
        self.test_multiple_enqueue_and_dequeue()
        print("All test cases passed!")

def main():
    TestQueue()

if __name__ == "__main__":
    main()