def concatenate_strings():
    num_strings = int(input("Enter the number of strings: "))
    result = ""
    for i in range(num_strings):
        result += input(f"Enter string {i+1}: ") + " "
    print("Concatenated string: ", result)

concatenate_strings()