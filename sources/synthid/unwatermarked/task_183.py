def max_product(series, span):
    if len(series) < span:
        return "Invalid Input"
    
    max_prod = 0
    
    for i in range(len(series)-span+1):
        prod = 1
        for j in range(i, i+span):
            prod *= int(series[j])
        
        if prod > max_prod:
            max_prod = prod
            
    return max_prod

print(max_product("639815", 3))  # Output: 324
