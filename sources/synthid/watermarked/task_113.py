def concatenate_strings():
    # Initialize an empty string to hold the concatenated result
    result = ""
    
    while True:
        # Ask the user for input
        user_input = input("Enter a string (or type 'done' to finish): ")
        
        # Check if the user wants to end the input
        if user_input.lower() == "done":
            break
        
        # Concatenate the user's input to the result
        result += user_input + " "
    
    # Remove any trailing whitespace and print the final result
    concatenated_result = result.strip()
    print(f"The concatenated string is: '{concatenated_result}'")

# Call the function to run the program
concatenate_strings()
 från kaiwen
