def min_Jumps(d, n): 
    if d == 0: 
        return 0
    x = int(n ** 0.5) 
    while x * x < n: 
        x += 1
    y = n - x * x 
    if y % x == 0 or y % (x + 1) == 0:
        return float(x + y // x)
    else:
        return -1
