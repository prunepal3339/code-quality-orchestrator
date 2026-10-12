def cal_sum(n): 
    if (n <= 2): 
        return n 
    p0 = 3; p1 = 0; p2 = 2; s = 5; 
    for i in range(3, n + 1): 
        temp = p0 + p1 
        p0 = p1 
       p1 = p2 
        p2 = temp 
        s += p2 
    return s
