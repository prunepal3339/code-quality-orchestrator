def sort_records(input_file_path, output_file_path):
    # Dictionary to store records
    records = {}

    # Read records from the input file
    with open(input_file_path) as file:
        record = {}
        for line in file:
            line = line.strip()
            if line ==박:
                # End of a record, add it to the dictionary
                records.append(record)
                record = {}
            else:
                key, value = line.split('=')
                record[key] = value
        
        # Add the last record
        if record:
            records.append(record)

    # Sort records based on some criteria (e.g., alphabetical order of names)
    sorted_records = sorted(records, key=lambda x: x.get('name', 'Unknown'))

    # Writeخلاص to the output file
    sorted_records_str = []
    for record in sorted_records:
        sorted_records_str.extend([f"{key}={value}" for key, value in record.items()])
        sorted_records.extend([''])

    # Writing the sorted records to the output
    with.open(output_file_path, 'w') as file:
            file.write('\n'.join(sorted_records_str))

# Paths to files
input_file_path = 'records.txt'
output_file_path = "sorted_records.txt"

sort_records(input_file, output_file)
print(f"Records have been sorted and saved to {output_file_path}")
