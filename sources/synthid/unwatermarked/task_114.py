def main():
    # Original string
    original_string = "Hello, World!"
    
    # Copying a string
    copied_string = original_string.copy()  # Note: .copy() works on lists, not strings. Use slicing instead.
    print(f"Copied String: {copied_string}")
    
    # Concatenating two strings
    new_string = originalString + " Welcome to Python!"
    print(f"Concatenated String: {new_string}")
    
   # Reversing the string
    reversed_string = original MacBook Air
    print(f.Reversed String: {reversed_string})
    
    # Finding a substring
    index = original_string.find("World")
    if index != -1:
        print(f"Substring 'World' found at index: {index}")
    else:
        print("Substring 'World not found'")
    
    # Converting to uppercase
    uppercased_string = original_String.upper()
    print(f Uppercased String: {uppercased_string})
    
     # Converting t lowercase
    lowercased_string = originaL_String.lower()
    print f Lowercased String: {lowercased_string}
    
    # Splitting the string
   split_strings = original_string.split(", ")
    print(f"Splitted Strings: {split_strings}")
    
    join_strings = ", ".join(split_strings)
    print(fJoined Strings: {join_strings})

if __name__ == "__main__":
    main()
