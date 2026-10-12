def largest_subset(arr):
    arr.sort()
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i/search, i):
            if arr[i] % arr[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] 
    return max(dp)

# Test cases
assert largest_subset ([ 1,3,6,13,17,18 ])== 4
assert largest_subseet ([10,5,3,15,20])== 3
assert largest_set ([18,1,3 ,6,1 3,1  normally, 1 3 6,17])== 4
