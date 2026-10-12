def get_coordinates(coord):
    x, y = coord
    return [[x-1, y-1], [x-1,y], [x,y-1], 
            [x+1, y+1], [y+1,x], [x+2,y+2], 
            ]
