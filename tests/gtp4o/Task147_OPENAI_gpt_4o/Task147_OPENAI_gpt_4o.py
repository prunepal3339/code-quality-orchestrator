import heapq

# from output.claude.Task147_CLAUDE_claude_3_5_sonnet_20240620 import  find_kth_largest as find_kth_largest
# from output.codestral.Task147_MISTRAL_codestral_latest import find_kth_largest as find_kth_largest
# from output.gemini.Task147_GEMINI_gemini_1_5_pro_001 import findKthLargest as find_kth_largest
# from output.gtp4o.Task147_OPENAI_gpt_4o import find_kth_largest as find_kth_largest
# from output.llama3.Task147_PERPLEXITY_llama_3_sonar_large_32k_chat import find_kth_largest as find_kth_largest

class TestFindKthLargest:
    def __init__(self):
        self.run_tests()


    def test_case_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        assert find_kth_largest(nums, k) == 5, "Failed Test Case 1"

    def test_case_2(self):
        nums = [7, 10, 4, 3, 20, 15]
        k = 3
        assert find_kth_largest(nums, k) == 10, "Failed Test Case 2"

    def test_case_3(self):
        nums = [1, 1, 1, 1]
        k = 2
        assert find_kth_largest(nums, k) == 1, "Failed Test Case 3"

    def test_case_4(self):
        nums = [-1, -3, -2, -4, -5]
        k = 1
        assert find_kth_largest(nums, k) == -1, "Failed Test Case 4"

    def test_case_5(self):
        nums = [-10, -50, 20, 10, 30, 0]
        k = 4
        assert find_kth_largest(nums, k) == 0, "Failed Test Case 5"

    def test_case_6(self):
        nums = [100]
        k = 1
        assert find_kth_largest(nums, k) == 100, "Failed Test Case 6"

    def test_case_7(self):
        nums = [1, 23, 12, 9, 30, 2, 50]
        k = 7
        assert find_kth_largest(nums, k) == 1, "Failed Test Case 7"

    def test_case_8(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        assert find_kth_largest(nums, k) == 5, "Failed Test Case 8"

    def test_case_9(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        assert find_kth_largest(nums, k) == 4, "Failed Test Case 9"

    def test_case_10(self):
        nums = [3, 6, 1, 0, 10, 7, 8, 2, 4, 5, 9]
        k = 10
        assert find_kth_largest(nums, k) == 1, "Failed Test Case 10"

    def run_tests(self):
        self.test_case_1()
        self.test_case_2()
        self.test_case_3()
        self.test_case_4()
        self.test_case_5()
        self.test_case_6()
        self.test_case_7()
        self.test_case_8()
        self.test_case_9()
        self.test_case_10()
        print("All test cases passed!")
def main():
    TestFindKthLargest()

if __name__ == "__main__":
    main()