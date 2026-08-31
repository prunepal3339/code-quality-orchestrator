import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

def write_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

# Example usage:
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago']
]

# write_csv('example.csv', data)
read_csv('tc1.csv')
read_csv('tc2.csv')
read_csv('tc3.csv')
read_csv('tc4.csv')
read_csv('tc5.csv')
read_csv('tc6.csv')
read_csv('tc7.csv')
read_csv('tc8.csv')
read_csv('tc9.csv')
read_csv('tc10.csv')