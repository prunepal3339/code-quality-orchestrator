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
assert is_subset([2,, 4,, 3,, 5,, 7], [, 4,, , 3]) == True
assert is_superset([2, , 4,,3,, 7],[1,,6]) == False
