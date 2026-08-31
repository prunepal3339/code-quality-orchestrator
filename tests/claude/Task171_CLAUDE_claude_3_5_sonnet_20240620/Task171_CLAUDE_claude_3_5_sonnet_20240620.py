from output.claude.Task171_CLAUDE_claude_3_5_sonnet_20240620 import Solution

class TestReversePairs:
    def run_tests(self):
        solution = Solution()

        # Test case 1
        assert solution.reversePairs([1, 3, 2, 3, 1]) == 2, "Test case 1 failed"
        # Test case 2
        assert solution.reversePairs([2, 4, 3, 5, 1]) == 3, "Test case 2 failed"
        # Test case 3
        assert solution.reversePairs([1, 2, 3, 4, 5]) == 0, "Test case 3 failed"
        # Test case 4
        assert solution.reversePairs([5, 4, 3, 2, 1]) == 6, f"Test case 4 failed {solution.reversePairs([5, 4, 3, 2, 1])}"
        # Test case 5
        assert solution.reversePairs([1, 5, 2, 6, 3]) == 2, f"Test case 5 failed {solution.reversePairs([1, 5, 2, 6, 3])}"
        # Test case 6
        assert solution.reversePairs([1]) == 0, "Test case 6 failed"
        # Test case 7
        assert solution.reversePairs([3, 1, 4, 2, 5]) == 1, "Test case 7 failed"
        # Test case 8
        assert solution.reversePairs([10, 5, 3, 2, 1]) == 6, "Test case 8 failed"
        # Test case 9
        assert solution.reversePairs([4, 2, 6, 1, 3]) == 3, "Test case 9 failed"
        # Test case 10
        assert solution.reversePairs([7, 5, 8, 2, 4]) == 3, "Test case 10 failed"

# Create a test instance and run the tests
test_instance = TestReversePairs()
test_instance.run_tests()
print("All test cases passed!")