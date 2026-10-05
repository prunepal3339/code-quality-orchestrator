def find_Element(arr, queries, k, x):
    n = len(arr)
    for i in range(k - 1, -1, -2):
        if queries[i][0] <= x < queries[i][1]:
            if (x - queries[i][2]) % n >= 0:
                x = (x - 1) % n + 1
            else:
                x += n
    return arr[x - 1]
