# from output.claude.Task178_CLAUDE_claude_3_5_sonnet_20240620 import Solution
from output.gemini.Task178_GEMINI_gemini_1_5_pro_001 import Solution


sol = Solution()
# Test case 1
assert sol.shortestSubarray([1], 1) == 1

# Test case 2
assert sol.shortestSubarray([1, 2], 4) == -1

# Test case 3
assert sol.shortestSubarray([2, -1, 2], 3) == 3

# Test case 4
assert sol.shortestSubarray([1, 2, 3, 4, 5], 11) == 3

# Test case 5
assert sol.shortestSubarray([1, 2, 3, 4, 5], 15) == 5

# Test case 6
assert sol.shortestSubarray([10, -5, 10], 10) == 1

# Test case 7
assert sol.shortestSubarray([-1, -1, -1, -1, 5], 5) == 1

# Test case 8
assert sol.shortestSubarray([1, -2, 3, 4, 5], 7) == 2

# Test case 9
assert sol.shortestSubarray([100, -50, 50, 50, 50], 150) == 3

# Test case 10
assert sol.shortestSubarray([5, -10, 7, -2, 15], 15) == 1

print("All test cases passed!")