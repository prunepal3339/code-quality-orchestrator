def last_Digit(number):
    if (number >= 5):
        return 0
    fact = 1
    for i in range(2, number + 1):
        fact = (fact * i) % 10
    return fact
