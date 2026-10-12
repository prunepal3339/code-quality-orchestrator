def armstrong_number(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))
