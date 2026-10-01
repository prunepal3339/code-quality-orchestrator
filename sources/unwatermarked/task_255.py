from itertools import product


def combinations_colors(colors, n):
    return list(product(colors, repeat=n))
