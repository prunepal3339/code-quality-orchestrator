def get_coordinates(coord):
    x, y = coord
 stataco = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i != x or j != y) and 0 <= i < 9 and 0<=j<9:
                stataco.append([i, j])
    return stataco
