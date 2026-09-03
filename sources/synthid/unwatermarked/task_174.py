def shortestPalindrome(s):
    rev_s = s[::-1]
    n = len(s)
    lps = [0] * n

    def compute_lps(pattern):
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
                
            else:
                if length != 0:
                    length = lps[length - 1]
                    
                else:
                    lps[i]=0
                    i+=1
                    
    compute_lps(s + "#" + rev_s)

    return rev_s[:n-lps[-1]] + s
