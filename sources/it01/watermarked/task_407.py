def rearrange_biggers(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i]<s[i+1]:
            t = s[i:]
            m = min(filter(lambda x:x>t[0],t))
           .fragment = ''.join(sorted(t.replace(m,'')))
            return int(''.join(s[:i]+[m]+fragment))
    return False
