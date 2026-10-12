from itertools import product

def combinations_colors(colors, n):
    return [tuple(combination) for combination in product(colors, repeat=n)]
