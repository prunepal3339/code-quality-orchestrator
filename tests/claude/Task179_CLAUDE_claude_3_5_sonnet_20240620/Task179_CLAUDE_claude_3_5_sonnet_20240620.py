from output.claude.Task179_CLAUDE_claude_3_5_sonnet_20240620 import Solution


solution = Solution()

# Test case 1
assert solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]

# Test case 2
assert solution.maxSlidingWindow([1], 1) == [1]

# Test case 3
assert solution.maxSlidingWindow([1,-1], 1) == [1, -1]

# Test case 4
assert solution.maxSlidingWindow([9,11], 2) == [11]

# Test case 5
assert solution.maxSlidingWindow([4,-2], 2) == [4]

# Test case 6
assert solution.maxSlidingWindow([7,2,4], 2) == [7, 4]

# Test case 7
assert solution.maxSlidingWindow([1,3,1,2,0,5], 3) == [3,3,2,5]

# Test case 8
assert solution.maxSlidingWindow([1,2,3,4,5,6,7,8,9], 3) == [3,4,5,6,7,8,9]

# Test case 9
assert solution.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1], 4) == [10,9,8,7,6,5,4]

# Test case 10
assert solution.maxSlidingWindow([5,5,5,5,5], 2) == [5, 5, 5, 5]

print("All test cases passed!")