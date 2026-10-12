def median_numbers(x,y,z):
    if (y<x<z) or (z<x<y): 
        return float(x)
    elif (x<y<z)  or (z<y<x):
        return float(y)
    else:
        return float(z)
