def all_Bits_Not_Set(n, l, r): 
    mask = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1))
    return (n & mask) == 0
