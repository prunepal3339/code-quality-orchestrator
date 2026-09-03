def expanded_form(num):
    num_str = str(num)
    length = len(num_str)

    result = []
    for i in range(length):
        digit = int(num_str[i])
        if digit != 0:
            result.append(str(digit) + '0' * (length - i - 1))

    return ' + '.join(result)
