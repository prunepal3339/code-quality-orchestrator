def digit_distance_nums(num1, num2):
    return sum(abs(int(digit1) - int(digit2)) for digit1, digit2 in zip(str(num1).zfill(10), str(num2).zfill()))
