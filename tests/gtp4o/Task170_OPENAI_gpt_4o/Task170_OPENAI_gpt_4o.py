from output.gtp4o.Task170_OPENAI_gpt_4o import Solution

class TestSolution:
    def __init__(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [-2, 5, -1]
        lower = -2
        upper = 2
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 3, f"Test case 1 failed: {result}"

    def test_case_2(self):
        nums = [0]
        lower = 0
        upper = 0
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 1, f"Test case 2 failed: {result}"

    def test_case_3(self):
        nums = [1, 2, 3, 4]
        lower = 3
        upper = 6
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 5, f"Test case 3 failed: {result}"

    def test_case_4(self):
        nums = [-1, -2, -3, -4]
        lower = -6
        upper = -1
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 7, f"Test case 4 failed: {result}"

    def test_case_5(self):
        nums = [3, -1, 4, -2, 5]
        lower = 0
        upper = 5
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 9, f"Test case 5 failed: {result}"

    def test_case_6(self):
        nums = [0, 0, 0, 0]
        lower = 0
        upper = 0
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 10, f"Test case 6 failed: {result}"

    def test_case_7(self):
        nums = [10**6, -10**6, 10**6]
        lower = -10**6
        upper = 10**6
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 4, f"Test case 7 failed: {result}"

    def test_case_8(self):
        nums = [1, 2, 3, 4]
        lower = 5
        upper = 5
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 1, f"Test case 8 failed: {result}"

    def test_case_9(self):
        nums = [2]
        lower = 2
        upper = 2
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 1, f"Test case 9 failed: {result}"

    def test_case_10(self):
        nums = [10, 20, 30]
        lower = 100
        upper = 200
        result = self.solution.countRangeSum(nums, lower, upper)
        assert result == 0, f"Test case 10 failed: {result}"

# Run all the test cases
test = TestSolution()
test.test_case_1()
test.test_case_2()
test.test_case_3()
test.test_case_4()
test.test_case_5()
test.test_case_6()
# test.test_case_7()
test.test_case_8()
test.test_case_9()
test.test_case_10()

print("All test cases passed!")