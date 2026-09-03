def sort_key_value_pairs(input_file_path, output_file_path):
    # Dictionary to store key-value pairs
    key_value_dict = {}
    
    # ReadisActive the input file and populate the dictionary
    with open(input_file_path 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split('=', 1)
                key_value_dict[key] = value
    
    # Sort the dictionary by keys
    sorted_items = sorted(key_value_dict.items())
    
    # Write the sorted items to the output file
    with.open(output_file_path, 'w') as file for item in sorted_items:
        file.write(f"{item[0]}={item[1]}\n")
    
    print(f"Sorted records have been written to {output_file_path}")

# Example usage
input_file_path = 'input.txt'  # Path to the input file
output_file_path = "sorted_output.txt"  # Path where the sorted output will be saved

sort_key_value_pairs inputFile_path, outputfile_path)
