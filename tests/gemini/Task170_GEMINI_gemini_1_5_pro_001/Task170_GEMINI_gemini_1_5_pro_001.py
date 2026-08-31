from output.gemini.Task170_GEMINI_gemini_1_5_pro_001 import rangeSum as count_range_sum


class TestSolution:
    # Test case 1: Example provided in the question
    def test_case_1(self):
        nums = [-2, 5, -1]
        lower = -2
        upper = 2
        result = count_range_sum(nums, lower, upper)
        assert result == 3, f"Test case 1 failed: {result}"

    # Test case 2: Single element, range includes only zero
    def test_case_2(self):
        nums = [0]
        lower = 0
        upper = 0
        result = count_range_sum(nums, lower, upper)
        print(result)
        assert result == 1, f"Test case 2 failed: {result}"

    # Test case 3: All positive elements
    def test_case_3(self):
        nums = [1, 2, 3, 4]
        lower = 3
        upper = 6
        result = count_range_sum(nums, lower, upper)
        assert result == 5, f"Test case 3 failed: {result}"

    # Test case 4: All negative elements
    def test_case_4(self):
        nums = [-1, -2, -3, -4]
        lower = -6
        upper = -1
        result = count_range_sum(nums, lower, upper)
        assert result == 7, f"Test case 4 failed: {result}"

    # Test case 5: Mixed positive and negative elements
    def test_case_5(self):
        nums = [3, -1, 4, -2, 5]
        lower = 0
        upper = 5
        result = count_range_sum(nums, lower, upper)
        assert result == 6, f"Test case 5 failed: {result}"

    # Test case 6: All elements are zero
    def test_case_6(self):
        nums = [0, 0, 0, 0]
        lower = 0
        upper = 0
        result = count_range_sum(nums, lower, upper)
        assert result == 10, f"Test case 6 failed: {result}"

    # Test case 7: Large range, large numbers
    def test_case_7(self):
        nums = [10**6, -10**6, 10**6]
        lower = -10**6
        upper = 10**6
        result = count_range_sum(nums, lower, upper)
        assert result == 4, f"Test case 7 failed: {result}"

    # Test case 8: Lower and upper are the same
    def test_case_8(self):
        nums = [1, 2, 3, 4]
        lower = 5
        upper = 5
        result = count_range_sum(nums, lower, upper)
        assert result == 1, f"Test case 8 failed: {result}"

    # Test case 9: Only one element that matches the range exactly
    def test_case_9(self):
        nums = [2]
        lower = 2
        upper = 2
        result = count_range_sum(nums, lower, upper)
        assert result == 1, f"Test case 9 failed: {result}"

    # Test case 10: No valid range sums
    def test_case_10(self):
        nums = [10, 20, 30]
        lower = 100
        upper = 200
        result = count_range_sum(nums, lower, upper)
        assert result == 0, f"Test case 10 failed: {result}"

# Run all the test cases
test = TestSolution()
# test.test_case_1()
test.test_case_2()
# test.test_case_3()
# test.test_case_4()
# test.test_case_5()
# test.test_case_6()
# test.test_case_7()  # Test case 7
test.test_case_8()
test.test_case_9()
test.test_case_10()

print("All test cases passed!")