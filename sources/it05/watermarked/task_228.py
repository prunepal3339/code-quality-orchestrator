def all_Bits_Not_Set(n, l, r): 
    mask = (~0) << (r + 1); 
    mask |= ((1 << l) - 1); 
    return (n & mask) == 0
