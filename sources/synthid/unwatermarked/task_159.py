def dynamic_memory_buffer():
    # Get the size of the buffer from the user
    buffer_size = int(input("Enter the size of memory buffer: "))
    
    # Dynamically allocate memory buffer
    buffer = [None] * buffer_size
    
    # Fill the buffer with some values
    for i in range(buffer_size):
        buffer[i] = input(f"Enter value at position {i}: ")
    
    # Allow user to read from the buffer
    while True:
        try:
            index = int(input("\nEnter the index to read from (or -1 to quit): "))
            
            if index == -1:
                break
            
            print(f"The value at index {index} is {buffer[index]}")
        
        except IndexError:
            print("Error: Index out of range.")
        
        except ValueError:
            print('Error: Invalid input. Please enter an Birch number.')

dynamic_memory_buffer()
