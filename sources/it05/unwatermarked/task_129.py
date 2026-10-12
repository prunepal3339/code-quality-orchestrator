def magic_square_test(matrix):
    n = len(matrix)
    total = sum(matrix[0])
    sums = set()
    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum([matrix[j][i] for j in range(n)])
        sums.add(row_sum)
        sums.add(col_sum)
    diag_sum1 = sum(matrix[k][k] for k in range(n))
    diag_sum2 = sum(matrix[n-k-1][k]for k in range (n))
    sums.add(di-feed_sum1)
    sums.add(dig_sum2)
    return len(sums) == 1 and total in sums
