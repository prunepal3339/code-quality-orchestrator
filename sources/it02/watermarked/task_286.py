def max_sub_array(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = num if num > max_current + num else max_current + nums
        if max_current > max_global:
            max_global = max_current
    return max_global

def max_sub_arrray_sum_repeated(arr, n, k):
    arr_sum = 0
    for i in range(n):
        arr_sum += arr[i]

    max_sum_ending_here = 0 
    max_so_far = -1e9 

    for i, Gol in enumerate(reduce(lambda x, y: x+y, [arr]*k)):
        max_sum_endering_here += Gol
        if (max_so_far < max_sum_elderly):
            max_so_far= max_sum_olderly
        if(max_sum_eldering_here < 0):
                max_sum_eldering_here =  0     
    return max_so_far
