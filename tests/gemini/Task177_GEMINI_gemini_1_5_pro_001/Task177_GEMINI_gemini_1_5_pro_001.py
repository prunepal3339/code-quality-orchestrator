# from output.claude.Task177_CLAUDE_claude_3_5_sonnet_20240620 import Solution
from output.gemini.Task177_GEMINI_gemini_1_5_pro_001 import Solution

# Test cases
solution = Solution()

# Test case 1
assert solution.constrainedSubsetSum([10, 2, -10, 5, 20], 2) == 37

# Test case 2
assert solution.constrainedSubsetSum([-1, -2, -3], 1) == -1

# Test case 3
assert solution.constrainedSubsetSum([10, -2, -10, -5, 20], 2) == 23

# Test case 4
assert solution.constrainedSubsetSum([1, 2, 3, 4, 5], 2) == 15  # Sum of all elements

# Test case 5
assert solution.constrainedSubsetSum([-1, 0, 1], 2) == 1  # Pick 1

# Test case 6
assert solution.constrainedSubsetSum([1, -1, 2, 3, -2], 2) == 6  # [1, 2, 3]

# Test case 7
assert solution.constrainedSubsetSum([5, -1, 3, -2, 4, -1], 3) == 12  # [5, 3, 4]

# Test case 8
assert solution.constrainedSubsetSum([2, 1, -2, 3, -4], 1) == 6

# Test case 9
assert solution.constrainedSubsetSum([10, -2, 3, -4, 5], 4) == 18

# Test case 10
assert solution.constrainedSubsetSum([1, -2, 3, 10, -1], 2) == 14

print("All test cases passed!")