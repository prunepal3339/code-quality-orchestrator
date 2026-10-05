import math

def babylonian_squaresqrt(number):
    if number == 0:
        return 0
    estimate = number / 2.0
    while True:
        next_estimate = (estimate + number / estimate) / 2
        if abs(next_estimate - estimate) < 1e-7:
            break
        estimate = next_estimate
    return estimate
