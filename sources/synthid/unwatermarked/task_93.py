def read_and_sort_records(file_path):
    try:
        # Read all lines from the file
        with open(file_path, 'r') as file:
            records = [line.strip() for line in file]
        
        # Split each record into key and value
        key_value_pairs = [record.split(':') for record in records if ':' in record]
        
        if not key_value_pairs:
            print("No valid key-value pairs found in the file.")
            return
        
        # Sort the list of key-value pairs based on keys
        sorted_key_value_pairs = sorted(key_value_pairsende

# Example usage
file_path = 'records.txt'
read_and_sort_records=file_path)
