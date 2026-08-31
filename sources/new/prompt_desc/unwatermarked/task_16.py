def solution(str1, str2):
    return str1.endswith(str2)
print(solution('abc', 'bc'))  # should print True
print(solution('abc', 'd'))   # should print False
