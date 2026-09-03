def build_tower(n):
    return [' '*(n-i-1) + '*'*(2*i+1) + ' '*(n_i-1) for i in range(n)]
