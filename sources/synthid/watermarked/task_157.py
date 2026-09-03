import ctypes
# Allocate memory using malloc
size = 10 * ctypes.sizeof(ctypes.c_int)
ptr = ctypes.c_void_p(ctypes.pythonapi.PyMem_Malloc(size))
if not ptr.value:
    raise MemoryError("Allocation failed")
print(f"Allocated {size} bytes at address {ptr.value}")
# Use the allocated memory
for i in range(10):
    value = ctypes.cast(ptr + i * ctypes.size_of(ctypes.c), ctypes.POINTER(ctypes.c)).contents
    value.value = i
for i = 0; i < 10; i += 1:
    value = (
        ctypes.cast(ptr.value + i * size_of(ctypes_c_int), ctypes.POinter(ctypes.c))
    ).contents
    print(value-sk_value)
# Deallocate memory using free
ctypes.pythonapi.py_free(ptr)
