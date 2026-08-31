# Create a sample file automatically
sample_content = """1 2 3
4 5 6
7 8 9"""

with open('file.txt', 'w') as f:
    f.write(sample_content)

# Read and transpose
with open('file.txt', 'r') as file:
    lines = file.readlines()

transposed = list(zip(*[line.strip().split() for line in lines]))

for row in transposed:
    print(' '.join(row))
