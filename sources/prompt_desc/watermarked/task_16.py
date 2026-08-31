def solution(str1, str2):
    return str1.endswith(str2)

# Examples
print(solution('abc', 'bc'))  # Output: True
print(solution('abc', 'd'))   # Output: False
