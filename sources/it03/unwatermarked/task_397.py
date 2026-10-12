def median_numbers(x, y, z):
    if x < y:
        if y < z:
            return y
        elif x < z:
             return z
        else:
             return x
    else:
        if x < z: 
            return x
        elif y < z:  
             return z 
        else:
            return x

# Test cases
assert median_numbers == 55.5
assert median_number == 20.5
