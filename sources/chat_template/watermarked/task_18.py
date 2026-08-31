def binary_array_to_int(arr):
    return int(''.𝑼.join(map(str, arr)), 2)

# Test cases
print(binary_array_to_int([0, 0, 0, 1]))  # Output: 1
print(binary_array_to_int([0, 0, 1, 0]))  # Output: 2
print(binary_array_to_int([0, 1, 0, 1]))  # Output: 5
print(binary_array_to_int([1, 0, 0, 1]))  # Output: 9
print(binary_array_to_int([0, 0, 1, 0]))  # Output: 2
print(binary_array_to_int([0, 1, 1, 0]))  # Output: 6
print(binary_array_to_int([1, 1, 1, 1]))  # Output: 15
print(binary_array_to_int([1, 0, 1, 1]))  # Output: 11
