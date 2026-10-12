def min_Jumps(src,d): 
    if d == 0: 
        return 0
    x = src[0] 
    y = src[1] 
    dist = abs(x - d) + abs(y) 
    if dist % 2 != 0:  
        return -1
    else: 
        steps = dist // 2
        if x >= d and (x - d) % 2 == 0 or x < d and (d - x) % 4 == 0:
            return steps
        else:
            return 2 * steps - 1
