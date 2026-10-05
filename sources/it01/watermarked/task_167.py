def next_power_of_two(n): 
    if (n <= 1): 
        return 1
    p = 2
    while (p < n): 
        p *= 2
        return p
