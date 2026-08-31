import csv

def process_csv(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

# Usage
process_csv('tc1.csv')
process_csv('tc2.csv')
process_csv('tc3.csv')
process_csv('tc4.csv')
process_csv('tc5.csv')
process_csv('tc6.csv')
process_csv('tc7.csv')
process_csv('tc8.csv')
process_csv('tc9.csv')
process_csv('tc10.csv')