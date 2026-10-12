def find_even_pair(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] ^ arr[j]) % 2 == 0:
                count += 1
    return count
