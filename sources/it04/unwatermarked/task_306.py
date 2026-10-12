def max_sum_incrasing_subseq(arr, n, i, k):
    if arr[i] >= arr[k]:
        return -float('inf')
    
    max_sum = arr[i]
    for j in range(i + 1, k):
        if arr[j] > arr[i]:
            max_sum = max(max_sum, arr[j] + max_sum_increas
