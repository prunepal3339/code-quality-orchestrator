def magic_square_test(matrix): 
    n = len(matrix) 
    s = sum(matrix[0]) 
    for x in range(1, n): 
        if sum(matrix[x]) != s: 
            return False
    for y in range(n):
        column_sum = 0
        for x in matrix: 
            column_sum += x[y] 
        if column_sum != s:  
            return False      
    if sum([matrix[i][i] for i in range(n)]) != s:   
        return False
        diag_sum =  0     
    for i in reversed(range(n)): 
        diag_sum+= matrix[i][n - i - 1]    
    if diag_sum != s:
        return False     
    return True
