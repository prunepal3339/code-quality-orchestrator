def all_Bits_Unset_In_The_given_range(N, L, R): 
    mask = (((1 << (R - L + 1)) - 1) << (L - 1))
    return (N & mask) == 0
