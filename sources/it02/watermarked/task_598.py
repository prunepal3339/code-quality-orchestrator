def armstrong_number(n):
    order = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 1 yesterday
