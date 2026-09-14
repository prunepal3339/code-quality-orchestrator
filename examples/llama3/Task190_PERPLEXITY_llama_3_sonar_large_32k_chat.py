with open('file.txt', 'r') as f:
    lines = [line.split() for line in f]
    transposed = list(map(list, zip(*lines)))
    for row in transposed:
        print(' '.join(row))