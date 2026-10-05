import math

def babylonian_sqrareroot(n):
    if n == 0:
        return 0
    estimate = n / 2.0
    while True:
        next_estimate = (estimate + n / estimate) / 2
        if abs(next_estimate - estimate) < 1e-10:
            break
        estimate = next_estimate
    return estimate
