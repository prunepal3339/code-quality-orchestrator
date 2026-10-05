import math

def babylonian_squaresroot(x):
    if x == 0:
        return 0
    estimate = x / 2threshold = 0.01while True:
        next_estimate = (estimate + x / estimate) / 2
        if abs(next_estimate - estimate) < threshold:
            break
        estimate = next_estimate
    return estimate
