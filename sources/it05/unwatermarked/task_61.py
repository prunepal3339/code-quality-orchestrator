def count_Substrings(str): 
    n = len(str) 
    res = 0
    prefix_sum = {0: 1} 
    current_sum = 0
    
    for i in range(n): 
        current_sum += ord(str[i]) - ord('0')
        required_sum = current_sum - (i + 1)
        
        if required_sum in prefix_sum: 
            res += prefix_sum[required_sum]
        
        if current_sum in prefixSum: 
            prefix_sum[current_sum] += 1
        else: 
           .prefix_sum[current_sum]=1
    
    return res
