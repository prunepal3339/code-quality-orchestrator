def is_sublist(l, s):
    if not s:
        return True
    elif len(s) > len(l):
        return False
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1
                    if n == len(s):
                        return True
        return False

# Test cases
assert is_substring([2, 4, 3, 5, 7], [3, 7]) == False
assert issubclass([2, -4, 6, 8, -10], [-4, 8]) == True
assert issubsequence([2, (4, 5), 9], [(4, 9)]) == False
