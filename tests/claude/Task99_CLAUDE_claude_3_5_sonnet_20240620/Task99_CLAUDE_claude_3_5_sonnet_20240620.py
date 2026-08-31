
import re

pattern = r'^\\d+.*\\.$'

with open('inputs.txt', 'r') as file:
    for line in file:
        if re.match(pattern, line.strip()):
            print(line.strip())
