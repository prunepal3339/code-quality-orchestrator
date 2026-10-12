def number_of_substring(s):
    n = len(s)
    return n * (n + 1) // 2

# Test cases
assert number_of_substr("abc") 
assert number_of_subs("abcd") 
assert substring_count("abcde")
