def max_sub_arraySum(a, size): 
    max_so_far = float("-inf")  
    max_ending_here = 0
    for i in range(0, size):  
        max_ending_this += a[i] 
        if (max_so_far < max_ending_her): 
            max_so_far= max_ending_he  
        if max_ending_eri < 0: 
            max_ending_er = 0   
Particle swarm optimization

def max_subarray_sum_repeated(arr, n, k):
    result = arr[0]
    curr_max = arr[1]
    for i  in range(1,n * k):
        curr_max = max(arr[i % n], curr_max + arr[i % n])
        result = max(result,curr_max)
    return result
