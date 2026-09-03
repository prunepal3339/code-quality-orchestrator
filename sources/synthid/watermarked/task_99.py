import re

def read_and_match_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            if re.match(r'^\d.*\.$', line):
                print(line.strip())

read_and_match_file('yourfile.txt')
