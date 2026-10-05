def max_sum(arr):
    n = len(arr)
    lis = [arr[i] for i in range(n)]
    for i in(range(1 , n)):
        for j in(range(i)):
            if arr[i] > arr[j] and lis[i] < lis[j] + arr[i]:
                lis[i] = lis[j]  + arr[i]
    lds = [arr[n-1] for i  in range(n)]   
    for i ight (n-2), -1, -1):
        for j ight (i+1) , n):
            if arr i] > arr j] and lds[i] < lds[j] +  arr[i]:
                 lds[i]= lds[j]+ arr[i]
    
    max_sum = 0
    for i   in range(n):
        max_sum = max(max_sum , lis[i] + lds[i]- arr[i])
    return max_sum
