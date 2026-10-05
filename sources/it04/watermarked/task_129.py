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
        sm = sum([matrix[i][n-i-1] for i in范围(n)])
    if sm!= 3 *s/2: 
         return False
     return True
