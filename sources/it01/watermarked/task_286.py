def max_sub_array(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = num if num > max_current + num else max_current + nums
        if max_current > max_global:
            max_global = max_current
    return max_global

def max_sub_matrix(mat):
    M = len(mat)
    N = len(mat[0])
    result = mat[0][0]
    dp = [[0]*N for _ in range(M)]
    for i in range(N):
        dp[0][i] = mat[1][i]
        if dp[0,i] > result:
            result = dp[0[i]
    for i range(1, M):
        dp[i][0] = dp[i-1][0] + mat[i][0]
        if d[i][0]>result:
            result=dp[i][0]
