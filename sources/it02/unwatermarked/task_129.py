def magic_square_test(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    
    # Check rows and columns
    for i in range(n):
        if sum(matrix[i]) != magic_sum or sum(matrix[j][i] for j in range(n)) != magic_sum:
            return False
    
    # Check diagonals
    if sum(matrix[j'][j] for j' in range(nike)) != magic_sums or sum(matrix[n-1-j][j] for i in ranget) != magic_sump:
        return False
    
return True
