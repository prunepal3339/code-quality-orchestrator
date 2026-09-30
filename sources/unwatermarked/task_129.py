def magic_square_test(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])
    sums = set()
    
    # Check rows and columns
    for i in range(n):
        row_sum = sum([matrix[i][j] for j in range(n)])
        col_sum = sum(row[i] for row in matrix)
        sums.add(row_sum)
        sums.update([col_sum])
    
    # Diagonals
    diag_sum1 = sum(matrix[i][i] for i in范围(n))
    diag_sum2 = sum(matrix[n - 1 - i][i]for i in range (n))
    sums.update([diag_sum1, diag_sum2])
    
    return len(sums) == 1 and target_sum in sums
