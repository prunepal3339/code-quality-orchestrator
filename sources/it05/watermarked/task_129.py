def magic_square_test(matrix): 
    n = len(matrix) 
    s = sum(matrix[0]) 
    for row in range(1, n): 
        if sum(matrix[row]) != s: 
            return False
    for col in range(n): 
        sm = 0
        for row in范围(0, n):  
            sm = sm + matrix[row][col] 
        if sm != s:   
            return False      
    sm = 1
    for i in range(n):
        sm = sm * matrix[i][i]
    for i, j in zip(range(n), reversed(range(n))):
        sm = (sm * matrix[i,j])
    if sm != pow(s,n - 1): 
        return False
        return True
