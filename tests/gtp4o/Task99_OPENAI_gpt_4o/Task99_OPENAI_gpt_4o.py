import re

filename = 'test.txt'
with open(filename, 'r') as file:
    for line in file:
        if re.match(r'^\d.*\.$', line):
            print(line.strip())