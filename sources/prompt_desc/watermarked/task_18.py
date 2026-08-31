def binary_array_to_int(binary_array):
    # Convert binary array to string
    binary_string = ''.join(map(str, binary_array))
    
    # Convert binary string to integer
    decimal_number = int(binary_string, 2)
    
    return decimal_number

# Examples
examples = [
    [0, 0, 0, 1],   # Expected output: 1
    [0, 0, 1, 0],   # Expected output: 2
    [0, 1, 0, 1],   # Expected output: 5
    [1, 0, 0, 1],   # Expected output: 9
    [0, 0, 1, 0],   # Expected output: 2
    [0, 1, 1, 0],   # Expected output: 6
    [1, 1, 1, 1],   # Expected output: 15
    [1, 0, 1, 1]    # Expected output: 11
]

for example in examples:
    print(f"Testing: {example} ==> {binary_array_to_int(example)}")
