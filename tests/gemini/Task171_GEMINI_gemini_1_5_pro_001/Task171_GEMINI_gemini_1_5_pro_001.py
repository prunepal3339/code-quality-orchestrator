from output.gemini.Task171_GEMINI_gemini_1_5_pro_001 import Solution

class TestReversePairs:
    def run_tests(self):
        solution = Solution()  # Instantiate the Solution class

        # Test case 1
        nums1 = [1, 3, 2, 3, 1]
        assert solution.reversePairs(nums1) == 2, f"Test case 1 failed: {nums1}"

        # Test case 2
        nums2 = [2, 4, 3, 5, 1]
        assert solution.reversePairs(nums2) == 3, f"Test case 2 failed: {nums2}"

        # Test case 3
        nums3 = [1, 2, 3, 4, 5]
        assert solution.reversePairs(nums3) == 0, f"Test case 3 failed: {nums3}"

        # Test case 4
        nums4 = [5, 4, 3, 2, 1]
        assert solution.reversePairs(nums4) == 6, f"Test case 4 failed: {nums4}"

        # Test case 5
        nums5 = [1, 5, 2, 6, 3]
        assert solution.reversePairs(nums5) == 3, f"Test case 5 failed: {nums5}"

        # Test case 6
        nums6 = [1]
        assert solution.reversePairs(nums6) == 0, f"Test case 6 failed: {nums6}"

        # Test case 7
        nums7 = [3, 1, 4, 2, 5]
        assert solution.reversePairs(nums7) == 2, f"Test case 7 failed: {nums7}"

        # Test case 8
        nums8 = [10, 5, 3, 2, 1]
        assert solution.reversePairs(nums8) == 7, f"Test case 8 failed: {nums8}"

        # Test case 9
        nums9 = [4, 2, 6, 1, 3]
        assert solution.reversePairs(nums9) == 3, f"Test case 9 failed: {nums9}"

        # Test case 10
        nums10 = [7, 5, 8, 2, 4]
        assert solution.reversePairs(nums10) == 4, f"Test case 10 failed: {nums10}"

# Main function to run the tests
if __name__ == "__main__":
    test_instance = TestReversePairs()
    test_instance.run_tests()
    print("All test cases passed!")