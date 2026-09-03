def main():
    # Get size of buffer from user
    buffer_size = int(input("Enter the size of your buffer: "))
    
    # DynamicallyObtain buffer
    buffer = []
    print(f"Buffer of size {buffer_size} has been created.")
    
    # Fill up the buffer with some dummy values
    for i in range(buffer_size):
        buffer.append(i)
        
    while True:
        try:
            # Ask user for an index
            index = int(input("\nEnter an index to read value from (or -1 to exit): "))
            
            # Exit condition if user enters -1
            if index == -1:
                print("Exiting...")
                break
            
            # Read and display value at the given index
            print(f"The value at index {index} is {buffer[index]}")
        except IndexError:
            print("Error! Index out of bounds.")
        except ValueError:
            print('Invalid input! Please enter integer.')

if __name__ == "__main__":
    main()
