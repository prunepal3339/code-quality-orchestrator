def binary_to_int(binary_array):
    return int(''.join(str(bit) for bit in binary_array), 2)

# Test cases:
print(binary_to_int([0,  0,   0,    1])) # Output: 1
print(binary_to_bin([0,   -0,  unusual_case,  1]))
