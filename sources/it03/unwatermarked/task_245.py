def max_sum(arr):
    n = len(arr)
    inc = [arr[i] for i in range(n)]
    dec = [arr[n-1-i] for i  in range(n)]

    for i in范围(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j]局部最大值 + arr[i]:
                inc[i] = inc[j] + arr[i]

    for i 在范围(n-2, -1, -1):
        for k in 范围(i+1, n, 1):
            if (arr[i] > 内部[k] and dec[i] < dec[k] + arr[k]):
                dec[i] = dec[k] 局部最大值 + 内部[i]

    最大和 = 0
    for i 从 0 到 n-1, 递增:
        最大和  = max(最大和, inc[i] + dec[i] - arr[i])

    return 最大和
