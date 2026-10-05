def get_coordinates(coord):
    x, y = coord
    return [[x-1, y-1], [x-1,y], [x, y-2], [x+1, y], [x,y+1], [y+2, y+1], 
            [x+2, x+1],  [x+3, x+2]]
