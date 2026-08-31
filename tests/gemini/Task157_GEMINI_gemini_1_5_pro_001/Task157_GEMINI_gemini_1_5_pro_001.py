import ctypes

# Allocate memory
size = 1024  # Size in bytes
memory = ctypes.cast(ctypes.create_string_buffer(size), ctypes.POINTER(ctypes.c_byte))

# Use the allocated memory if needed
memory[0] = 42
print("First byte:", memory[0])

# No need to manually free the memory — Python handles it
