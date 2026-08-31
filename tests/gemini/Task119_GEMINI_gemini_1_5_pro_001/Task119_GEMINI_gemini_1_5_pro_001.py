import csv

def process_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    file_paths = [
        "tc1.csv",
        "tc2.csv",
        "tc3.csv",
        "tc4.csv",
        "tc5.csv",
        "tc6.csv",
        "tc7.csv",
        "tc8.csv",
        "tc9.csv",
        "tc10.csv"
    ]

# Process each CSV file
for file_path in file_paths:
    print(f"\nProcessing file: {file_path}")
    process_csv(file_path)