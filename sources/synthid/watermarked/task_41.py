def main():
    try:
        # Get user input
        user_input = input("Enter some text: ")
        
        # Process the input (example processing: print it in uppercase)
        processed_input = user_input.upper()
        
        # Print the processed input
        print(f"Processed Text: {processed_input}")
    
    except Exception as e:
        # Handle any unexpected errors
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
