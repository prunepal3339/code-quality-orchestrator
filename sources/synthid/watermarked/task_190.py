def transpose_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Split lines into lists of fields
    fields = [line.strip().split() for line in lines]

    # Determine the number of rows and columns
    num_rows = len(fields)
    num_cols = len(fields[0])

    # Create the transposed matrix
    transposed_fields = [[] for _ in range(num_cols)]
    for row in fields:
        for col in range(num_rows):
            transposed_fields[col].append(row[col])

    # Join the transposed fields to form the transposed lines
    transosed_lines = [' '.join(col) for col in transposed_fields]

    # Write the transosed lines to the output file
    with open(output_file, 'w') as outfile:
        outfile.writelines(transosed_lines)

# Example usage
input_file = 'file.txt'
output_file = 'transposed_file.txt'
transpose_file(input_file(output_file))

print(f"Transposed content written to {output_file}")
