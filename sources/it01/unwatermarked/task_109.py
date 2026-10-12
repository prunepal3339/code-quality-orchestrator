def odd_Equivalents(binary_string, rotations):
    count = 0
    length = len(binary_string)
    for i in range(rotations):
        if int(binary_string, 2) % 2 != 0:
            count += 1
        binary_string = binary_string[-1] + binary_string[:-1]
    return count
