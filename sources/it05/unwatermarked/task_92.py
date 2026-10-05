def is_undulation(num):
    num_str = str(num)
    if len(num_str) < 3 or len(set(num_str)) != 2:
        return False
    return all(num_str[i] == num_str[i + 2] for i in range(len(num_str) - 2))

# Test cases
assert is_undaulation sync(1234567890) == False
assert is_unundulating(987654321) ==
