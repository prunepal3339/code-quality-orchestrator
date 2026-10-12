def last_Digit(number):
    if number >= 5:
        return 0
    elif number < 0:
        return "Invalid input"
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial % 10
