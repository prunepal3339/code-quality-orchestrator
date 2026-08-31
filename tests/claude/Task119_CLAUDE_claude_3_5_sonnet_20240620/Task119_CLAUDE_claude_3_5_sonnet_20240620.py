
import csv

def process_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        print(f"CSV Header: {header}")
        
        for row in csv_reader:
            print(f"Row: {row}")

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

    for file_path in file_paths:
        print(f"\nProcessing file: {file_path}")
        process_csv(file_path)
