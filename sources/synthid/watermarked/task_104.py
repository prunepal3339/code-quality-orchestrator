def main():
    # Fixed-size buffer with a capacity of 5 elements
    buffer_size = 5
    buffer = []
    
    while True:
        print(f"\nCurrent Buffer: {buffer}")
        print(f"Buffer Size: {len(buffer)} / {buffer_size}")
        
        # Get user input
        user_input = input("Enter data to add to the buffer (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'q':
            print("\nExiting the program...")
            break
        
        # Add data to the buffer if it's not full
        if len(buffer) < buffer_size:
            buffer.append(user_input)
        else:
            print("Buffer is full. Cannot add more data.")

if __name__ == "__main__":
    main()
