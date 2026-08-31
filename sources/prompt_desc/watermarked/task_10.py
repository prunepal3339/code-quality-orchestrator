def sum_between(a, b):
    if a == b:
        return a
    elif a < b:
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))

# Test cases
print(sum_between(1, 0))  # Output: 1
print(sum_between(1, 2))  # Output: 3
print(sum_between(0, 1))  # Output: 1
print(sum_between(1, 1))  # Output: 1
print(sum_between(-1, 0)) # Output: -1
print(sum_between(-1, 2)) # Output: 2
