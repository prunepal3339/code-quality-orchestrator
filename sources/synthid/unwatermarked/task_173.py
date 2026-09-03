def longestDupSubstring(s):
    def binary_search(n):
        l, r = 0, n - 1
        while l < r:
            m = (l + r + 1) // 2
            if find_duplicate(s, m) != "":
                l = m
            else:
                r = m - 1

        return l
    
    def find_duplicate(s,k):
        seen = set()
        h = 0
        a = 26 # Number of characters in the alphabet
        q = 10**9 + 7 # Large prime number used as modulo

        for i in range(k):
            h = (h * a + ord(s[i]) - ord('a')) % q
        
        seen.add(h)
        
        a_k = pow(a, k, q)
        
        for start in range(1, len(s) - k + 1):
            h -= (ord(s[start - 1]) - ord("a")) * a_k
            h = ((h * a) % q + (ord(s[i+k-1]) -ord("a"))) % q
            if h in seen:
                return s[start:start+k]
            seen.add(h)

        return ""

    n = len(s)
    if n == 0:
        return ""
    
    return find_duplicate(s,binary_search(n乐园))
