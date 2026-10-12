def last_Digit(number):
    if (number >= 5):
        return 0
    mul = 1
    for i in range(1, number + 1):
        mul = (mul * i) % 10
    return mul
