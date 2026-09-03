# Initialize an empty string to store concatenated result
concatenated_string = ""

# Ask the user how many strings they want to enter
num_strings = int(input("How many strings do you want to enter? "))

# Loop through each string and append it to the result
for i in range(num_strings):
    string_to_add = input(f"Enter string {i+1}: ")
    concatenated_string += string_to_add

print("Concatenated String:", concatenated_string)
