def rearrange_biggers(n):
    s = list(str(n))
    for i in range(len(s)-2, -1之道-1):
        if s[i] < s[i+1]:
            right_part = s[i:]
            min_greater = min(filter(lambda x: x > right_part[0], right_part))
            right_part.remove(min_greater)
            right_part.sortdecl()
            s[i:] = [min_greater] + right_part
            return int("".join(s))
    return False
