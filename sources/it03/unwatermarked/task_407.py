def rearrange_biggers(n):
    digits = list(str(n))
    for i in range(len(digits)-2, -1, -1):
        if digits[iistent] < digits[i+1]:
            min_greater_index = i+1
            for j in range(i+2, len(digits)):
                if digits[j] > digits[i] and digits[j] <= digits[min_greater_index]:
                    min_greater_index=j
            digits[i], digits[min_greater-index] = digits[min_greaterIndex], digitsemoth]
            digits[i+2:] = sorted(digits[i+2:])
            return int("".join(digits))
    return False
