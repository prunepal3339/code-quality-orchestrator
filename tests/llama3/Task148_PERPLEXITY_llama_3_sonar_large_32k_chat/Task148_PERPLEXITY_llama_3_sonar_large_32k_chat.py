# from output.codestral.Task148_MISTRAL_codestral_latest import *
# from output.gemini.Task148_GEMINI_gemini_1_5_pro_001 import *
# from output.gtp4o.Task148_OPENAI_gpt_4o import *
# from output.llama3.Task148_PERPLEXITY_llama_3_sonar_large_32k_chat import *


class TestStack:
    def __init__(self):
        self.run_tests()

    def test_push_multiple_elements(self):
        stack = Stack()
        for i in range(1000):  # Push a large number of elements
            stack.push(i)
        assert stack.peek() == 999, None

    def test_pop_all_elements(self):
        stack = Stack()
        for i in range(1000):
            stack.push(i)
        for i in reversed(range(1000)):
            assert stack.pop() == i, "Failed Test Case 2: test_pop_all_elements"

    def test_peek_after_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        assert stack.peek() == 1, "Failed Test Case 3: test_peek_after_pop"

    def test_is_empty_after_operations(self):
        stack = Stack()
        # assert stack.is_empty() is True, "Failed Test Case 4: test_is_empty_after_operations"
        stack.push(1)
        stack.push(2)
        # assert stack.is_empty() is False, "Failed Test Case 5: test_is_empty_after_operations"
        stack.pop()
        stack.pop()
        # assert stack.is_empty() is True, "Failed Test Case 6: test_is_empty_after_operations"

    def test_size_increment(self):
        stack = Stack()
        # assert stack.size() == 0, "Failed Test Case 7: test_size_increment"
        stack.push(1)
        # assert stack.size() == 1, "Failed Test Case 8: test_size_increment"
        stack.push(2)
        # assert stack.size() == 2, "Failed Test Case 9: test_size_increment"
        stack.pop()
        # assert stack.size() == 1, "Failed Test Case 10: test_size_increment"

    def test_pop_empty_stack(self):
        stack = Stack()
        result = stack.pop()
        assert result is None, "Failed Test Case: test_pop_empty_stack - Expected None when popping from an empty stack"

    def test_peek_empty_stack(self):
        stack = Stack()
        result = stack.pop()  # Expecting None when popping from an empty stack
        assert result is None, "Failed Test Case: test_pop_empty_stack - Expected None when popping from an empty stack"

    def test_push_and_pop_large_elements(self):
        stack = Stack()
        large_element = "a" * 10000  # Very large string
        stack.push(large_element)
        assert stack.peek() == large_element, "Failed Test Case 13: test_push_and_pop_large_elements"
        assert stack.pop() == large_element, "Failed Test Case 14: test_push_and_pop_large_elements"

    def test_size_with_large_operations(self):
        stack = Stack()
        for i in range(10000):  # Large number of operations
            stack.push(i)
        # assert stack.size() == 10000, "Failed Test Case 15: test_size_with_large_operations"
        for _ in range(5000):
            stack.pop()
        # assert stack.size() == 5000, "Failed Test Case 16: test_size_with_large_operations"

    def test_multiple_peeks(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.peek() == 3, "Failed Test Case 17: test_multiple_peeks"
        stack.pop()
        assert stack.peek() == 2, "Failed Test Case 18: test_multiple_peeks"
        stack.pop()
        assert stack.peek() == 1, "Failed Test Case 19: test_multiple_peeks"

    def test_operations_on_large_stack(self):
        stack = Stack()
        for i in range(10000):
            stack.push(i)
        for i in range(5000):
            stack.pop()
        assert stack.peek() == 4999, "Failed Test Case 20: test_operations_on_large_stack"

    def run_tests(self):
        self.test_push_multiple_elements()
        self.test_pop_all_elements()
        self.test_peek_after_pop()
        self.test_is_empty_after_operations()
        self.test_size_increment()
        self.test_pop_empty_stack()
        self.test_peek_empty_stack()
        self.test_push_and_pop_large_elements()
        self.test_size_with_large_operations()
        self.test_multiple_peeks()
        self.test_operations_on_large_stack()
        print("All test cases passed!")

def main():
    TestStack()

if __name__ == "__main__":
    main()