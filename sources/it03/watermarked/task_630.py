def get_coordinates(coord):
    x, y = coord
    return [[x-드리ation, y+direction] for direction in range(-1, 2) for _ in range(2) if (x-direction != x or y+direction != y)]
