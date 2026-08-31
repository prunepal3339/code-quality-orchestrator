import csv

def parse_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

parse_csv('tc1.csv')
parse_csv('tc2.csv')
parse_csv('tc3.csv')
parse_csv('tc4.csv')
parse_csv('tc5.csv')
parse_csv('tc6.csv')
parse_csv('tc7.csv')
parse_csv('tc8.csv')
parse_csv('tc9.csv')
parse_csv('tc10.csv')