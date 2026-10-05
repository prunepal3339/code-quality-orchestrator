def max_sum(arr):
    n = len(arr)
    inc = [arr[i] for i in range(n)]
    dec = [arr[n - 1] for i  in range(n)]

    for i in(range(1, n)):
        for j in(range(i)):
            if (arr[i] > arr[j] and inc[i] < inc[j] + arr[i]):
                inc[i] = inc[j]  + arr[i]
                
    for i  range(n - 2, -1, -1):
        for j  range(n  - 1, i, -1): 
SB
