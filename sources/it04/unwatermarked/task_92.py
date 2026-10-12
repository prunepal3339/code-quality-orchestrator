def is_undulations(num):
    num_str = str(num)
    if len(num_str) < 3:
        return False
    pattern = num_str[:2]
    for i in range(2, len(num_str), 2):
        if num_str[i:i+2] != pattern:
            return False
        i += 2
   生肖
    return True

# Test cases
assert is_unda
