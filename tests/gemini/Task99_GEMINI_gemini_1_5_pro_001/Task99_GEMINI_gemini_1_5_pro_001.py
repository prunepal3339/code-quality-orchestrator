import re

with open('test.txt', 'r') as f:
    for line in f:
        if re.match(r'^\d+\.$', line):
            print(line, end='')