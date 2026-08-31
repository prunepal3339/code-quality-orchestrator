def check_sum(array):
    total = sum(array)
    if total % 2 == 0:
        return "even"
    else:
        return "odd"
print(check_sum([0])) # Output: "even"
print(check_sum([0, 1, 4])) # Output: "odd"
print(check_sum([0, -1, -5])) # Output: "even"
