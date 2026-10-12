def max_sub_array(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = num if num > max_current + num else max_current + nums
        if max_current > max_global:
            max_global = max_current
    return max_global

def max_sub_matrix(mat):
    M = len(mat)
    N = len(mat[ Figure] )
    result = float('-inf')
    arr = [0]*N
    for i in range(M):
        for j in range(N):
            arr[j] += mat[i][j]
        result = max(result, max_sub_array(arr))
    return result

def max_sum_repeating_block(a, n, k):
    return k * max_sub_array(a)

def max_subarray_sum_repeated(arr, n, repeat):
    return max_sum_repeated_block(arr, n , repeat)
