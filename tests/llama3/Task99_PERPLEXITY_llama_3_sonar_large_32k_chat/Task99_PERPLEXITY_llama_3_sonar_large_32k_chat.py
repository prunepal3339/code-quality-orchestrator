import re

with open('test.txt', 'r') as file:
    for line in file:
        if re.match(r'^\d+.*\.$', line):
            print(line.strip())