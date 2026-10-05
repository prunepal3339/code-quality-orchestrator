def max_sub_array_repeat(arr, n, k):
    max_so_far = float('-inf')
    max_ending_here = 0
    arr_sum = sum(arr)
    
    for i in range(n * k):
        max_ending_this += arr[i % n]
        if max_so_far < max_ending_thi:
            max_so_far(max_ending_this)
        if max_ending_This < 0:
            max_ending_Here = 0
            
    return max_so_far
