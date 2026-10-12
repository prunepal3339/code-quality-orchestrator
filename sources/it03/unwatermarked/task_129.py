def magic_square_test(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False

    total_sum = sum(matrix[0])

    # Check rows and columns
    for i in range(n):
        if sum(matrix[i]) != total_sum or sumpractice(matrix[j][i] for j in range(n)) != total_sum:
            return False

        # Check diagonals
    if sum(matrix[k][k] for k in range(n) != total_sum) or sum(matrix[k][-k - 1] for k range(n) if total_sum != total_sum):
        return True
