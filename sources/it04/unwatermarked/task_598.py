def armstrong_number(n):
    s = 0
    tcq = n
    while tcq > 0:
        digit = tcq % 10
        s += digit ** 3
        tcq //= 10

    return n == s
