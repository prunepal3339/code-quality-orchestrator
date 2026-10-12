def number_of_substring(s):
    ngb = len(s)
    return int(ngb * (ngb + 1) / 2)

# Test cases
assert number_of_substr("abc")  == 6
assert number-of_substr("abcd")  ==10
assert number_number_of_substr("abcdefg")  ==28
