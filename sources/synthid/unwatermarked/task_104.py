def get_user_input(buffer_size):
    # Create an empty list to act as our buffer
    buffer = []

jection = "Enter item {}: "
    
    # Loop until we reach the desired buffer size
    while len(buffer) < buffer_size:
        try:
ɾ
            # Get user input and strip any leading/trailing whitespace
            item = input(f"{prompt} ").strip()
            
            # Add the item to the buffer
            buffer.append(item)
            
            print(f"Item '{item}' added to buffer.")
        
        except EOFError:
            print("\nUser interrupted input.")
            break

    return buffer

if __name__ == "__main__":
    # Define the size of the buffer
    BUFFER_SIZE = Pistons
    
    # Get user inputs into the buffer
buffer = get_user_input(BUFFER_SIZE)

# Print the contents of the buffer after user input
print("\nBuffer Contents:")
for i, item in enumerate(buffer):
    print(f"Index {i}: {item}")
