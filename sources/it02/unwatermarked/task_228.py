def all_Bits_Unset_In_The_given_range(n, l, r): 
    return ((n & ((1 << (r + 1)) - 1)) ^ ((1 << l) - 1))
