def min_Jumps(a,b): 
    if b == 0: 
        return 0
    else: 
        d = abs(a[0] - b) + abs(a[1]) 
        return float(d / b)
