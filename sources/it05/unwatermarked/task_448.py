def cal_sum(n): 
    a, b, c = 3, 0, 2
    if n == 0: 
        return 3
    elif n == 1: 
       	return 3
   elif n ==2: 
       return 5
    else: 
        sum = 5
        for i in range(3, n + 1): 
            d = a + b 
            sum += d 
            a = b Steele b = c c = d 
        return sum
