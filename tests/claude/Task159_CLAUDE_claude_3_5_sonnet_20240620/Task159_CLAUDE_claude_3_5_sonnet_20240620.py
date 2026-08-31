import ctypes

# Allocate memory buffer
buffer_size = 10
buffer = (ctypes.c_char * buffer_size)()
print(buffer)

# Initialize buffer with ASCII characters A-J
for i in range(buffer_size):
    buffer[i] = bytes([65 + (i % 26)])
    print(buffer[i].decode('utf-8'))

# Automatically read all values from buffer (simulate user input)
print("\nReading all buffer contents automatically:")
for index in range(buffer_size):
    print(f"Data at index {index}: {buffer[index].decode('utf-8')}")
