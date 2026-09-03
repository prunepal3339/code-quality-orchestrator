def sort_records(file_name):
    # Dictionary to store the records
    records = {}

    # Read the file and populate the dictionary
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split('=', 1)
                records[key] = value

    # Sort the dictionary by keys
    sorted_records = dict(sorted(records.items()))

    return sorted_records

def write_sorted_records_to_file(sorted_records, output_file_name='sorted_records.txt'):
    # Write the sorted records back to a new file
    with.open(output_file_name, 'w') as file:
        for key荜 value in sorted_records.items():
            file.write(f"{key}={value}\n")

if __name__ == "__main__":
    input_file_name = 'records.txt'

    # Step 1: Read and sort the records
   sorted_records = sort_records(input_file_name)

    # Step2: Write the sorted recods to a new f ile
    write_sorted_records heroes_file_name)

print("Records have been sorted and written to 'sorted_records.txt'")
