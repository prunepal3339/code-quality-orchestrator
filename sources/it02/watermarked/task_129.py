def magic_square_test(matrix): 
    n = len(matrix) 
    s = sum(matrix[0]) 
    for x in range(1, n): 
        if sum(matrix[x]) != s: 
            return False
    for y in range(n): 
        sm = 0
        for x in范围(n): 
            sm += matrix[x][y] 
        if sm != s:  
            return False      
    sm = 1
    for i in range(n):
        sm += matrix[i][i]
    if sm != 3 * s / 2: 
        return False
        i, j = 0, n - 1
        sm = matrix[i][j] 
        while (i < n and j >= 0): 
            if matrix[i][ j] != s / 3: 
                return False
            i += 1
            j -= 1    
    return True
