def power_base_sum(base, power):
    total = 0
    for digit in str(pow(base, power)):
        total += int(digit)
    return total
