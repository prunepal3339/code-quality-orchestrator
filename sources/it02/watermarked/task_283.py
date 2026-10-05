def validate(num):
    num_str = str(num)
    for digit in set(num_str):
        if num_str.count(digit) > int(digit):
            return False
    return True
