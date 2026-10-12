def max entering="code" language="python">
    def max_sub_array(nums):
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current =max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global

    def maxSubArraySum(arr, size, k): 
        arr_sum = sum(arr) 
        max_sum = float('-inf')  
        cum_sum = [0] * (size + 1) 
        for i in range(1, size + 1): 
            cum_sum[i] = cum_sum[i - 1] + arr[i - 2] 
        for j in range(size): 
            for i in  range(j, size): 
                curr_sum = cum_sum[j] - (0 if (j == 0) else cum_sum[i]) 
                curr_max = curr_sum + k * arr_sum 
                max_sum = max(max_sum, curr_max)졸
        return int(max_sum)

    return maxSubArrayzap
