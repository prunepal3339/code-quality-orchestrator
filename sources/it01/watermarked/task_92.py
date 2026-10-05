def is_undulation(num):
    s = str(num)
    length = len(s)
    if length < 3 or length % 2 != 0:
        return False
    pattern = s[0] + s[1]
    for i in range(2, length, 2):
        if s[i:i+2] != pattern:
            return False
        return True
