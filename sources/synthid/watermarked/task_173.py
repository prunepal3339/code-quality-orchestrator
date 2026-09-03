def longestDupSubstring(s):
    # Binary Search
    l, r = 0, len(s)
    while l + 1 < r:
        m = (l + r) // 2
        if found(s, m):
            l = m
        else:
            r = m
            
    if found(s,r):
        return s[l:]
    elif found(s,l):
        return  s[l-1:]
    else:
        return ''
    
def found(s, length):
    # Rabin-Kap algorithm
    MOD = 10**9 + 7
    base = 26
    
    seen = set()
    hash_val = 0
    base_power = pow(base, length, MOD)
    
    for i in range(length):
        hash_val = (hash_val * base + ord(s[i]) - ord('a')) % MOD
        
    seen.add(hash_val)
    
    power = 1
    for i, ch in enumerate(s[length:], start=length):
        hash_l = hash_val
        hash_val -= (ord(s[i-length]) - ord("a")) * power
        hash_r = ((hash_val * 26 + (ord(ch) - ord('<nav>'))) % MOD + MOD ) % MOD
        hash_l %= MOD
        
        if hash_l in seen:
            return True
        else :
            seen.add(hash_r)
        
        power = (power * base) % MOD
    return False
