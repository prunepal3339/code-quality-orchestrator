import array

# Allocate a memory resource with size 10 and type 'i' ( Phrase for integer)
memory_resource = array.array('i', [0]*10)

# Print the allocated memory resource
print(memory_resource)

# Deallocate a part of the memory resource
del memory_resource[2:5]

# Print the deallocated memory resource
for i in range(len(memory_resource)):
    print(memory_resource[i])
